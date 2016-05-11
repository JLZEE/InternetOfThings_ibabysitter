'''
This code is for operating open fan commend, 
here provide 2 options: strong wind (level_1) and weak wind (level_0)
'''

import mraa
import time
 

def main():
	buzz_pin_number=6
	 
	# Configuring the switch and buzzer as GPIO interfaces

	fan = mraa.Gpio(buzz_pin_number)
	 
	# Configuring the switch and buzzer as input & output respectively

	fan.dir(mraa.DIR_OUT)
	 
	print "Press Ctrl+C to escape..."
	flag = True
	try:
		while(flag):
			fan.write(1)    # switch on the buzzer
			time.sleep(30) # puts system to sleep for 0.2sec before switching
			fan.write(0)    # switch off buzzer\
			print "Turn off fan..."
			#time.sleep(0.1)
			flag = False
	except KeyboardInterrupt:
		fan.write(0)
		exit

def level_0():
	buzz_pin_number=6
	fan = mraa.Gpio(buzz_pin_number)
	fan.dir(mraa.DIR_OUT)
	 
	print "Press Ctrl+C to escape..."
	i=0
	try:
		while(i<75):
			fan.write(1)    # switch on the buzzer
			time.sleep(0.2) # puts system to sleep for 0.2sec before switching
			fan.write(0)    # switch off buzzer\
			time.sleep(0.2)
			i += 1
		fan.write(0)
		print "Turn off fan..."
		#time.sleep(0.1)
	except KeyboardInterrupt:
		fan.write(0)
		exit

def level_1():
	buzz_pin_number=6
	fan = mraa.Gpio(buzz_pin_number)
	fan.dir(mraa.DIR_OUT)
	 
	print "Press Ctrl+C to escape..."
	i=0
	try:
		fan.write(1)    # switch on the buzzer
		time.sleep(30) # puts system to sleep for 0.2sec before switching
		fan.write(0)    # switch off buzzer\
		print "Turn off fan..."
		#time.sleep(0.1)
	except KeyboardInterrupt:
		fan.write(0)
		exit

if __name__ == '__main__':
	main()
