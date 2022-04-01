#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ledPin = 18
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)


def S():
    for i in range(3):
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledPin, GPIO.LOW)


def O():
    for i in range(3):
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1.5)
        GPIO.output(ledPin, GPIO.LOW)


try:
    while True:
        if GPIO.input(buttonPin) == GPIO.HIGH:
            S()
            O()
            S()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
