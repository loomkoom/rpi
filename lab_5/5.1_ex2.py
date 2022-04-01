#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin1 = 18
pin2 = 23
pin3 = 24
pin4 = 25
pins = [pin1,pin2,pin3,pin4]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)


def on():
    GPIO.output(pin1,1)
    GPIO.output(pin2,1)
    GPIO.output(pin3,1)
    GPIO.output(pin4,1)
    
def off():
    GPIO.output(pin1,0)
    GPIO.output(pin2,0)
    GPIO.output(pin3,0)
    GPIO.output(pin4,0)

try:
    while True:
        on()
        time.sleep(0.1)
        off()
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)