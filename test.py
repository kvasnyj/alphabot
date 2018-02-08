import RPi.GPIO as GPIO                          
import time             

GPIO.setmode(GPIO.BCM)                          
pir = 4                                        
GPIO.setup(pir, GPIO.IN)                          

print "Waiting for sensor to settle"
time.sleep(2)                                     
print "Detecting motion"

while True:
    val = GPIO.input(pir)
    print val
    time.sleep(2)                               
                            