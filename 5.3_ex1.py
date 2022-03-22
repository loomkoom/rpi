import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin = 17
GPIO.setup(pin, GPIO.IN)


try:
    while True:
        if (GPIO.input(pin) == 0):
            print("Dark")
            time.sleep(0.5)
        else:
            print("Light")
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
