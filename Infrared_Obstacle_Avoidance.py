import RPi.GPIO as GPIO
import time
from AlphaBot import AlphaBot

Ab = AlphaBot()

DR = 16
DL = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(DR,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(DL,GPIO.IN,GPIO.PUD_UP)

inert = 3

def right():
	print("right")

	Ab.stop()
	time.sleep(0.2)

	for i in range(inert): 
		Ab.right()
		time.sleep(0.2)

def left():
	print("left")

	Ab.stop()
	time.sleep(0.2)

	for i in range(inert): 
		Ab.left()
		time.sleep(0.2)

try:
	while True:
		DR_status = GPIO.input(DR)
		DL_status = GPIO.input(DL)
		if((DL_status == 1) and (DR_status == 1)):
			Ab.forward()
			print("forward")
		elif((DL_status == 1) and (DR_status == 0)):
			left()
		elif((DL_status == 0) and (DR_status == 1)):
			right()
		else:
			Ab.backward()
			time.sleep(0.2)
			Ab.left()
			time.sleep(0.2)
			Ab.stop()
			print("backward")

except KeyboardInterrupt:
	GPIO.cleanup();

