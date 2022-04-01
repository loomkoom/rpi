#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


try:
    while True:
        light = 0
        GPIO.setup(17, GPIO.OUT)
        GPIO.output(17, 0)
        time.sleep(0.2)
        GPIO.setup(17, GPIO.IN)
        while GPIO.input(17) == 0:
            light += 1
        print(light)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
