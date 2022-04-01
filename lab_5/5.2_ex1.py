#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
ledPin = 24
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)


def blink(pin):
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)
    time.sleep(0.5)


try:
    while True:
        print(GPIO.input(buttonPin))
        if GPIO.input(buttonPin) == GPIO.LOW:
            blink(ledPin)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
