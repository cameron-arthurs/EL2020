import Adafruit_DHT as DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.IN)
GPIO.setup(17,GPIO.OUT)

try:
	with open("../log/templog.csv", "a") as log:
		while True:
			input = GPIO.input(26)
			if input == True:
				temp,hum = DHT.read_retry(DHT.DHT11,17)
				temp = temp * 9/5.0 +32
				if hum is not None and temp is not None:
					tempFahr = '{0:0.1f}*F'.format(temp)
					print('Temperature = {0:0.1f}*F Humidity = {1:0.1f}%'.format(temp, hum))
					log.write("{0},{1}\n".format(time.strftime("%Y%m%d %H:%M:%S"),str(tempFahr)))
				else:
					print('Failed to get reading.')
except KeyboardInterrupt:
	GPIO.cleanup()
