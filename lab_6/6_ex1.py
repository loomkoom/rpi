#!/usr/bin/env python3
import cgitb; cgitb.enable()
import spidev
import time
import busio
import digitalio
import board
from adafruit_bus_device.spi_device import SPIDevice

# Initialize SPI bus
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialize control pins for adc
cs0 = digitalio.DigitalInOut(board.CE0)  # chip select
adc = SPIDevice(spi, cs0, baudrate=1000000)

# read SPI data 8 possible adc's (0 thru 7)


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
        tmp1 = readadc(1)  # read channel 1
        print("input 0:", tmp0, round(tmp0*(3.3/1023),2), "(V)")
        print("input 1:", tmp1, round(tmp1*(3.3/1023),2), "(V)", "\n")
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\nProgram Exited")
    exit(0)
