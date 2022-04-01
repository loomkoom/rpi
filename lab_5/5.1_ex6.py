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
    
def turn_on(pins):
    for pin in pins:
        GPIO.output(pin,GPIO.HIGH)
    
def turn_off(pins):
    for pin in pins:
        GPIO.output(pin,GPIO.LOW)


def short():
    turn_on(pins)
    time.sleep(0.5)
    turn_off(pins)
    
def long():
    turn_on(pins)
    time.sleep(1.5)
    turn_off(pins)

try:
    while True:
        short()
        long()
        short()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)