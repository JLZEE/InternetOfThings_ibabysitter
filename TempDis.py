'''
This code is for measuring temperature by using temperature sensor
'''


import pyupm_i2clcd as lcd
import time
import mraa
import math
'''
switch_pin_number=8

switch=mraa.Gpio(switch_pin_number)
switch.dir(mraa.DIR_IN)

myLcd=lcd.Jhd1313m1(0,0x3E,0x62)
myLcd.clear()
myLcd.setColor(200,200,0)
myLcd.setCursor(0,0)
'''
def main():
	B=4275
	try:
		time.sleep(10)
		tempSensor=mraa.Aio(1)
		a=tempSensor.read()
		R=1023.0/(float(a))-1.0
		temperature=1.0/(math.log(R)/B+1/298.15)-273.15
		#myLcd.setCursor(0,1)
		#myLcd.write(str(temperature))
		#time.sleep(2)
		#myLcd.clear()
		print temperature
		return str(temperature)

	except KeyboardInterrupt:
		exit

if __name__ == '__main__':
	print main()
