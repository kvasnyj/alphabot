import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)

i20 = -100
while True:
    i2 = GPIO.input(2)
    if i20 != i2:
        i20 = i2
        print(i2)