import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

def blinkOnce(pin):
	GPIO.output(pin,True)
	time.sleep(0.2)
	GPIO.output(pin,False)
	time.sleep(0.2)

for i in range(10):
	blinkOnce(17)

GPIO.cleanup()
