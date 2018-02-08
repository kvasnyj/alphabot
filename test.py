#!/usr/bin/python
import sys
import Adafruit_DHT

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

# import RPi.GPIO as GPIO


# GPIO.setmode(GPIO.BCM)
# GPIO.setup(2,GPIO.IN)

# i20 = -100
# while True:
#     i2 = GPIO.input(2)
#     if i20 != i2:
#         i20 = i2
#         print(i2)