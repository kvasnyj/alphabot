import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)

i2 = GPIO.input(2)
print(i2)