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
        GPIO.output(pin,1)
    
def turn_off(pins):
    for pin in pins:
        GPIO.output(pin,0)

try:
    while True:
        for pair in [(pin1,pin3),(pin2,pin4)]:
            turn_on(pair)
            time.sleep(1)
            turn_off(pair)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
        
        
