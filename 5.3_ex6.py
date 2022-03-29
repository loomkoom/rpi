import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dist_in_pin = 17
dist_out_pin = 27
led_pin = 26
pin1 = 12
pin2 = 16
pin3 = 20
pin4 = 21
pins = [pin1, pin2, pin3, pin4]
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
GPIO.setup(dist_in_pin, GPIO.IN)
GPIO.setup(dist_out_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.output(dist_out_pin, 0)
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
    GPIO.output(dist_out_pin, 1)
    time.sleep(0.00001)
    GPIO.output(dist_out_pin, 0)

    while not GPIO.input(dist_in_pin):
        pass
    signal_high = time.time()

    while GPIO.input(dist_in_pin):
        pass
    signal_low = time.time()
    delta_time = signal_low-signal_high
    distance = delta_time*17000
    return distance


try:
    while True:
        distance = round(measure_distance(),2)

        if distance > 30:
            GPIO.output(led_pin,0)
            GPIO.output(pin4,0)
            GPIO.output(pin2,0)
            GPIO.output(pin3,0)
            GPIO.output(pin1,0)
            print('safe: ', distance, "cm")
        else:
            while distance < 30:
                print('alarm: ', distance, "cm")
                GPIO.output(led_pin,1)
                full_step(pins + pins[0:2])
                distance = round(measure_distance(),2)
        time.sleep(0.1)


except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nProgram Exited")
    exit(0)
