#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)


try:
    while True:
        if (GPIO.input(17) == 0):
            print("Dark")
            time.sleep(0.5)
        else:
            print("Light")
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
