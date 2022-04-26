#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
from asyncio import start_server
from adafruit_bus_device.spi_device import SPIDevice
import spidev
import busio
import digitalio
import board
import adafruit_pcd8544
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import cgitb
cgitb.enable()
GPIO.setmode(GPIO.BCM)

DISTANCE_TRESHOLD = 30
LAMP_ON = "15:38"
LAMP_OFF = "15:39"
isLampOn = False
hasFed = False

trigPinOut = 25
echoPinIn = 24
GPIO.setup(trigPinOut, GPIO.OUT)
GPIO.setup(echoPinIn, GPIO.IN)
GPIO.output(trigPinOut, 0)

rstPin = 6
dcPin = 5

pumpPin = 13
GPIO.setup(pumpPin, GPIO.OUT)
GPIO.output(pumpPin, 1)

ledPin = 22
GPIO.setup(ledPin, GPIO.OUT)


# Initialize SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize control pins for adc
cs0 = digitalio.DigitalInOut(board.CE0)  # chip select
adc = SPIDevice(spi, cs0, baudrate=1000000)

# Initialize display
dc = digitalio.DigitalInOut(board.D6)  # data/command
cs1 = digitalio.DigitalInOut(board.CE1)  # chip select CE1 for display
reset = digitalio.DigitalInOut(board.D5)  # reset
display = adafruit_pcd8544.PCD8544(spi, dc, cs1, reset, baudrate=1000000)
display.bias = 4
display.contrast = 60
display.invert = True

#  Clear the display.  Always call show after changing pixels to make the display update visible!
display.fill(0)
display.show()

# Load default font.
font = ImageFont.load_default()
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 18)

# Get drawing object to draw on image
image = Image.new('1', (display.width, display.height)
                  )  # mode 1 is for monochrome
draw = ImageDraw.Draw(image)


stepPins = [12, 16, 20, 21]
for pin in stepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

btnPins = [23, 4, 17, 27]
btnvals = [0, 0, 0, 0]
for pin in btnPins:
    GPIO.setup(pin, GPIO.IN)


time.sleep(1)


def pair(pin_on, pin_off):
    GPIO.output(pin_on, 1)
    GPIO.output(pin_off, 0)


def full_step(seq):
    i = 0
    while i < 4:
        pin_on, pin_off = seq[i], seq[i+2]
        pair(pin_on, pin_off)
        time.sleep(0.01)
        i += 1
        
def motor_on(direction):
    if direction == "forwards":
        full_step(stepPins + stepPins[0:2])
    if direction == "backwards":
        full_step((stepPins + stepPins[0:2])[::-1])


def motor_off():
    GPIO.output(stepPins[0], 0)
    GPIO.output(stepPins[1], 0)
    GPIO.output(stepPins[2], 0)
    GPIO.output(stepPins[3], 0)

def measure_distance():
    GPIO.output(trigPinOut, 1)
    time.sleep(0.00001)
    GPIO.output(trigPinOut, 0)

    while not GPIO.input(echoPinIn):
        pass
    signal_high = time.time()

    while GPIO.input(echoPinIn):
        pass
    signal_low = time.time()
    delta_time = signal_low-signal_high
    distance = delta_time*17000
    return distance


try:
    while True:
        # manual buttons
        if (GPIO.input(btnPins[0]) == 1):
            if btnvals[0] == 0:
                print("Light turns on")
                btnvals[0] = 1
                GPIO.output(ledPin, 1)
                isLampOn = True
                time.sleep(0.5)
        else:
            if btnvals[0] == 1:
                print("Light turns off")
                btnvals[0] = 0
                GPIO.output(ledPin, 0)
                isLampOn = False
                time.sleep(0.5)

        if (GPIO.input(btnPins[1]) == 1):
            if btnvals[1] == 0:
                btnvals[1] = 1
                print("pump on")
                GPIO.output(pumpPin, 0)
                time.sleep(0.5)
        else:
            if btnvals[1] == 1:
                print("pump off")
                btnvals[1] = 0
                GPIO.output(pumpPin, 1)
                time.sleep(0.5)

        if (GPIO.input(btnPins[2]) == 1):
            if btnvals[2] == 0:
                btnvals[2] = 1
                print("stepper forward")
                stepper_on = time.time()
                while time.time() - stepper_on < 3:
                    motor_on("forwards")               
        else:
            if btnvals[2] == 1:
                print("stepper off")
                btnvals[2] = 0
                motor_off()

        if (GPIO.input(btnPins[3]) == 1):
            if btnvals[3] == 0:
                btnvals[3] = 1
                print("stepper backward")
                stepper_on = time.time()
                while time.time() - stepper_on < 3:
                    motor_on("backwards")     
        else:
            if btnvals[3] == 1:
                print("stepper off")
                btnvals[3] = 0
                motor_off()
                
        # automatic light
        human_time = time.strftime("%H:%M", time.localtime())
        if not isLampOn and human_time >= LAMP_ON:
            GPIO.output(ledPin, 1)
            isLampOn = True
        if isLampOn and human_time >= LAMP_OFF:
            GPIO.output(ledPin, 0)
            isLampOn = False
            
        # feed at set time:
        if not hasFed and human_time >= FEED_TIME:
            draw.rectangle((0, 0, display.width, display.height),
                       outline=255, fill=255)
            draw.text((1, display.height//2), "FEEDING", font=font)
            display.image(image)
            display.show()
            motor_on("forwards")
            isLampOn = True
        if hasFed and human_time >= FEED_TIME:
            GPIO.output(ledPin, 0)
            isLampOn = False       
            

        # pump when water too low
        distance = round(measure_distance(), 2)

        if distance > DISTANCE_TRESHOLD:
            motor_off()
            print('safe: ', distance, "cm")
        else:
            draw.rectangle((0, 0, display.width, display.height),
                       outline=255, fill=255)
            draw.text((1, display.height//2), "PUMPING", font=font)
            display.image(image)
            display.show()
            while distance < DISTANCE_TRESHOLD:
                print('alarm: ', distance, "cm")
                motor_on("forwards")
                distance = round(measure_distance(), 2)

        distance = round(measure_distance(), 2)

        draw.rectangle((0, 0, display.width, display.height),
                       outline=255, fill=255)

        draw.text((1, 0), human_time, font=font)
        draw.text((1, display.height//4*1), str(isLampOn), font=font)
        draw.text((1, display.height//4*2),
                  str(distance), font=font)
        draw.text((1, display.height//4*3), "fill", font=font)

        display.image(image)
        display.show()
        time.sleep(0.1)


except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
