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
buttonPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)


def turn_on_off(pin):
    GPIO.output(pin, 1)
    time.sleep(0.5)
    GPIO.output(pin, 0)


try:
    while True:
        print(GPIO.input(buttonPin))
        if GPIO.input(buttonPin) == GPIO.LOW:
            for pin in pins:
                turn_on_off(pin)
        else:
            for pin in pins[::-1]:
                turn_on_off(pin)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
