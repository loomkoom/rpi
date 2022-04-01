#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
in_pin = 17
btn_pin = 26
out_pin = 18
GPIO.setup(in_pin, GPIO.IN)
GPIO.setup(btn_pin, GPIO.IN)
GPIO.setup(out_pin, GPIO.OUT)


try:
    while True:
        if (not GPIO.input(in_pin) or not GPIO.input(btn_pin)):
            print("Dark")
            GPIO.output(out_pin,1)
            time.sleep(0.5)
        else:
            print("Light")
            GPIO.output(out_pin,0)
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
