import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
in_pin = 17
out_pin = 18
GPIO.setup(in_pin, GPIO.IN)
GPIO.setup(out_pin, GPIO.OUT)


try:
    while True:
        if (GPIO.input(in_pin) == 0):
            print("Dark")
            GPIO.output(out_pin,1)
            time.sleep(0.5)
        else:
            print("Light")
            GPIO.output(out_pin,1)
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
