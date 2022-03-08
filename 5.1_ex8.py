import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pins = [18,23,24,25]
pwms = []
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,GPIO.LOW)
    pwm = GPIO.PWM(pin, 1000)
    pwm.start(0)
    pwms.append(pwm)

try:
    while True:
        for dc in range(25,125,25):
            for pwm in pwms:
                pwm.ChangeDutyCycle(dc)
            time.sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)