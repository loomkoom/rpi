#!/usr/bin/env python3
import RPi.GPIO as GPIO
from adafruit_bus_device.spi_device import SPIDevice
import board
import digitalio
import busio
import time
import spidev
import cgitb
cgitb.enable()
pin1 = 23
pin2 = 24
hysteris_gap = 50
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)


# Initialize SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize control pins for adc
cs0 = digitalio.DigitalInOut(board.CE0)  # chip select
adc = SPIDevice(spi, cs0, baudrate=1000000)

# read SPI data 8 possible adc's (0 thru 7)


def readadc(adcnum):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    with adc:
        r = bytearray(3)
        spi.write_readinto([1, (8+adcnum) << 4, 0], r)
        time.sleep(0.000005)
        adcout = ((r[1] & 3) << 8) + r[2]
        return adcout


try:
    while True:
        tmp0 = readadc(0)  # read channel 0
        tmp1 = readadc(1)  # read channel 1
        print("input 0:\t", tmp0, "\t", round(tmp0*(3.3/1023), 2), "V")
        print("input 1:\t", tmp1, "\t", round(tmp1*(3.3/1023), 2), "V")
        if (tmp0 > tmp1) and abs(tmp0-tmp1) > hysteris_gap:
            GPIO.output(pin1, 1)
            GPIO.output(pin2, 0)
            print("led 1 on")
        elif (tmp1 > tmp0) and abs(tmp0-tmp1) > hysteris_gap:
            GPIO.output(pin2, 1)
            GPIO.output(pin1, 0)
            print("led 2 on")
        print()
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
