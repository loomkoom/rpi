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

def turn_on_off(pin):
    GPIO.output(pin,1)
    time.sleep(0.5)
    GPIO.output(pin,0)
    
def alternate():
    for pin in [pin1,pin2,pin3,pin4,pin3,pin2]:
        turn_on_off(pin)

try:
    while True:
        alternate()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
        
        
