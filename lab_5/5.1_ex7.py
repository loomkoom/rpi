#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)


def blink(pin,blink_amount,period,duty_cycle):
    time_high = period * duty_cycle/100
    time_low = period - time_high
    for counter in range(blink_amount):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(time_high)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(time_low)

try:
    while True:
        blink(18,20,0.5,75)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
        
