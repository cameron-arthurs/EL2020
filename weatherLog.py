import RPi.GPIO as GPIO
import Adafruit_DHT
import Adafruit_BMP.BMP085 as BMP #library used for the barometric pressure sensor module 
import time
import os
import sqlite3 as sql
import smtplib

redPin = 27
greenPin = 22
tempPin = 17

tempSensor = Adafruit_DHT.DHT11 #temperature & humidity sensor

presSensor = BMP.BMP085 #Barometric Pressure sensor

#LED variables
blinkDur = .1
blinkTime = 7

#sql database connection
con = sql.connect('weatherLog.db')
cur = con.cursor()
eChk = 0

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(greenPin,GPIO.OUT)

def readDHT(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not Not:
		tempF = '{0:0.1f}'.format(temperature)
		humid = '{1.0.1f}'.format(temperature, humidity)
	else:
		print('Error reading temperature sensor')

	return tempF, humid

def readPressure():
	pressure = presSensor.read_pressure()
	if pressure is not None:
		presF = '{0:0.2f}'.format(pressure) #formatted pressure reading
	else:
		print('Error reading pressure sensor')

	return presF


oldTime = 60

tempF, humid = readDHT(tempPin)
presF = readPressure()

try:
	while True:
		if time.time() - oldTime > 59:
			tempF, humid = readDHT(tempPin)
			presF = readPressure()
			cur.execute('INSERT INTO weatherLog values(?,?,?,?)', (time.strftime('%Y-%m-%d %H:%M:%S'),tempF,humid,presF)) #inserts date/time, temperature, humidity, and air pressure into the database
			con.commit()

			table = con.execute("select * from weatherLog")
			os.system('clear')
			for row in table:
				print "%-30s %-20s %-20s %-20s" %(row[0], row[1], row[2], row[3])
			oldTime = time.time()

except KeyboardInterrupt:
	os.system('clear')
	con.close()
	print("Weather Logging system & web app exited cleanly")
	exit(0)
	GPIO.cleanup
