import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin1 = 18
pin2 = 23
pin3 = 24
pin4 = 25
buttonPin = 17
pins = [pin1, pin2, pin3, pin4]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)


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


try:
    while True:
        print(GPIO.input(buttonPin))
        if GPIO.input(buttonPin) == GPIO.LOW:
            full_step(pins + pins[0:2])
        else:
            full_step((pins + pins[0:2])[::-1])


except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
