#!/usr/bin/env python3 
import RPi.GPIO as GPIO
import time
from datetime import datetime
GPIO.setmode(GPIO.BCM)

DISTANCE_TRESHOLD = 30
LAMP_ON = 8
LAMP_OFF = 20
isLampOn = False;

trigPinOut = 24
echoPinIn = 25
GPIO.setup(trigPinOut, GPIO.IN)
GPIO.setup(echoPinIn, GPIO.OUT)
GPIO.output(trigPinOut, 0)

rstPin = 6
dcPin = 5

ledPin = 22
GPIO.setup(ledPin, GPIO.OUT)

stepPins = [12,16,20,21]
for pin in stepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

btnPins = [23, 4, 17, 27]
for pin in btnPins:
    GPIO.setup(pin, GPIO.INPUT)

pumpPin = 13


time.sleep(1)

def pair(pin_on, pin_off):
    GPIO.output(pin_on, 1)
    GPIO.output(pin_off, 0)


def full_step(seq):
    i = 0
    while i < 4:
        pin_on, pin_off = seq[i], seq[i+2]
        pair(pin_on, pin_off)
        time.sleep(0.01)
        i += 1


def measure_distance():
    GPIO.output(trigPinOut, 1)
    time.sleep(0.00001)
    GPIO.output(trigPinOut, 0)

    while not GPIO.input(echoPinIn):
        pass
    signal_high = time.time()

    while GPIO.input(echoPinIn):
        pass
    signal_low = time.time()
    delta_time = signal_low-signal_high
    distance = delta_time*17000
    return distance


try:
    while True:
        # manual buttons 
        if (GPIO.input(btnPins[0]) == 0):
            print("Light turns on")
            GPIO.output(ledPin,1)
            isLampOn = True;
            time.sleep(0.5)
        else:
            print("Light turns off")
            GPIO.output(ledPin,0)
            isLampOn = False;
            time.sleep(0.5)

        if (GPIO.input(btnPins[1]) == 0):
            print("pump on")
            GPIO.output(pumpPin,1)
            time.sleep(0.5)
        else:
            print("pump off")
            GPIO.output(pumpPin,0)
            time.sleep(0.5)

        if (GPIO.input(btnPins[2]) == 0):
            print("stepper forward")
            full_step(stepPins + stepPins[0:2])
            time.sleep(0.5)
        else:
            print("stepper off")
            GPIO.output(stepPins[0],0)
            GPIO.output(stepPins[1],0)
            GPIO.output(stepPins[2],0)
            GPIO.output(stepPins[3],0)
            time.sleep(0.5)

        if (GPIO.input(btnPins[3]) == 0):
            print("stepper backward")
            full_step((pins + pins[0:2])[::-1])
            time.sleep(0.5)
        else:
            print("stepper off")
            GPIO.output(stepPins[0],0)
            GPIO.output(stepPins[1],0)
            GPIO.output(stepPins[2],0)
            GPIO.output(stepPins[3],0)
            time.sleep(0.5)
        # automatic light
        time = time.strftime("%H:%M",time.localtime())
        if not isLampOn and time > LAMP_ON  :
            GPIO.output(ledPin,1)
            isLampOn = True;
        if not  isLampOn and time > LAMP_OFF:
            GPIO.output(ledPin,0)
            isLampOn = False

        # pump when water too low
        distance = round(measure_distance(),2)

        if distance > DISTANCE_TRESHOLD:
            GPIO.output(stepPins[0],0)
            GPIO.output(stepPins[1],0)
            GPIO.output(stepPins[2],0)
            GPIO.output(stepPins[3],0)
            print('safe: ', distance, "cm")
        else:
            while distance < DISTANCE_TRESHOLD:
                print('alarm: ', distance, "cm")
                GPIO.output(ledPin,1)
                full_step(stepPins + stepPins[0:2])
                distance = round(measure_distance(),2)
        time.sleep(0.1)


except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
