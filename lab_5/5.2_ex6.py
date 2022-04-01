#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ledPin1 = 18
ledPin2 = 25
buttonPin1 = 17
buttonPin2 = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin1, GPIO.OUT)
GPIO.setup(ledPin2, GPIO.OUT)
GPIO.setup(buttonPin1, GPIO.IN)
GPIO.setup(buttonPin2, GPIO.IN)

try:
    while True:
        print(GPIO.input(buttonPin1), " ", GPIO.input(buttonPin2))
        GPIO.output(ledPin1, GPIO.input(buttonPin1))
        GPIO.output(ledPin2, GPIO.input(buttonPin2))
        time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
