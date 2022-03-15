import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin1 = 18
pin2 = 23
pin3 = 24
pin4 = 25
pins = [pin1, pin2, pin3, pin4]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)


def turn_on_off(pin):
    GPIO.output(pin, 1)
    time.sleep(0.01)
    GPIO.output(pin, 0)


def wave_drive():
    for pin in [pin1, pin2, pin3, pin4]:
        turn_on_off(pin)


try:
    while True:
        wave_drive()

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
