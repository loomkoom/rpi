#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def blink(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,1)
    time.sleep(0.5)
    GPIO.output(pin,0)
    time.sleep(0.5)
    
try:
    while True:
        blink(24)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)