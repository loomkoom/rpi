#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
in_pin = 18
out_pin = 17
GPIO.setup(in_pin, GPIO.IN)
GPIO.setup(out_pin, GPIO.OUT)
GPIO.output(out_pin, 0)
time.sleep(1)

try:
    while True:
        
        GPIO.output(out_pin, 1)
        time.sleep(0.00001)
        GPIO.output(out_pin, 0)
        
        while not GPIO.input(in_pin):
            pass
        signal_high = time.time()

        while GPIO.input(in_pin):
            pass
        signal_low = time.time()
        delta_time = signal_low-signal_high
        distance = delta_time*17000
        print(distance)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)