# PWM on two LED's

import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM

GPIO.setup(14, GPIO.OUT)# set GPIO 14 as output for green led
GPIO.setup(15, GPIO.OUT)# set GPIO 15 as output for red led

green = GPIO.PWM(14, 100)    # create object white for PWM on port 14 at 100 Hz
red = GPIO.PWM(15, 100)      # create object red for PWM on port 15 at 100 Hz

green.start(0)              # start green led on 0 percent duty cycle (off)
red.start(100)              # red fully on (100%)

# dim/brighten the leds, so one is bright while the other is dim

pause_time = 0.05           # you can change this to slow down/speed up

try:
	while True:
		for i in range(0,101):      # 101 because it stops when it finishes 100
			green.ChangeDutyCycle(i)
			red.ChangeDutyCycle(100 - i)
			time.sleep(pause_time)

		for i in range(100,-1,-1):      # from 100 to zero in steps of -1
			green.ChangeDutyCycle(i)
			red.ChangeDutyCycle(100 - i)
			time.sleep(pause_time)

except KeyboardInterrupt:
	green.stop()            # stop the white PWM output
	red.stop()              # stop the red PWM output
	GPIO.cleanup()          # clean up GPIO on CTRL+C exit