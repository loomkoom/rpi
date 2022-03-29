# PWM DC motor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

yellow = GPIO.PWM(14, 100)
green = GPIO.PWM(15, 100)

yellow.start(0)
green.start(100)


pause_time = 0.05
try:
    while True:
        time.sleep(5)
        yellow.ChangeDutyCycle(100)
        time.sleep(2)
        green.ChangeDutyCycle(0)
        time.sleep(5)
        green.ChangeDutyCycle(100)
        time.sleep(2)
        yellow.ChangeDutyCycle(0)

except KeyboardInterrupt:
    yellow.stop()
    green.stop()
    GPIO.cleanup()
