import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)

i2 = GPIO.input(3)
print(i2)