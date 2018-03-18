import RPi.GPIO as GPIO
import time
from AlphaBot import AlphaBot

SERVO = 27

Ab = AlphaBot()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(SERVO, GPIO.OUT, initial=GPIO.LOW) 
p = GPIO.PWM(SERVO,50)
p.start(0)

def ServoAngle(angle):
	p.ChangeDutyCycle(2.5 + 10.0 * angle / 180)

ServoAngle(90)	