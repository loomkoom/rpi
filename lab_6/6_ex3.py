#!/usr/bin/env python3
import RPi.GPIO as GPIO
from adafruit_bus_device.spi_device import SPIDevice
import board
import digitalio
import busio
import time
import spidev
import cgitb
cgitb.enable()


spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs0 = digitalio.DigitalInOut(board.CE0)  # chip select
adc = SPIDevice(spi, cs0, baudrate=1000000)


def readadc(adcnum):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    with adc:
        r = bytearray(3)
        spi.write_readinto([1, (8+adcnum) << 4, 0], r)
        time.sleep(0.000005)
        adcout = ((r[1] & 3) << 8) + r[2]
        return adcout


try:
    while True:
        tmp0 = readadc(0)  # read channel 0
        temp = round(((5*tmp0*100)/1023), 2)
        print("input 0:\t", tmp0, "\t", temp, "°C")
        print()
        time.sleep(0.4)
except KeyboardInterrupt:
    print("\nProgram Exited")
    exit(0)
