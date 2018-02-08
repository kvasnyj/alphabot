import RPi.GPIO as GPIO
import time

TRIG = 2
ECHO = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)

def Distance():
    	GPIO.output(TRIG,GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(TRIG,GPIO.LOW)
	while not GPIO.input(ECHO):
		pass
	t1 = time.time()
	while GPIO.input(ECHO):
		pass
	t2 = time.time()
	return (t2-t1)*34000/2


while True:
        middleDistance = Distance()
    print("MiddleDistance = %0.2f cm"%middleDistance)    