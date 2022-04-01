#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
pin = 17
GPIO.setmode(GPIO.BCM)


try:
    while True:
        light = 0
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)
        time.sleep(0.2)
        GPIO.setup(pin, GPIO.IN)
        while GPIO.input(pin) == 0:
            light += 1
        print(light)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
