import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:
    if (GPIO.input(17)==0):
        print("Dark")
        time.sleep(0.5)
    else:
        GPIO.output(18,0)
        print("Light")
        time.sleep(0.5)
        