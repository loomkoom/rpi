#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

while True:
    if (GPIO.input(17)==0):
        print("button pressed")
        GPIO.output(18,1)
        time.sleep(0.3)
    else:
        GPIO.output(18,0)
        print("button released")
        time.sleep(0.3)
        