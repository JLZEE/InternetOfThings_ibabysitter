'''
This code is used on raspberry pi client, sending prediction result to server
'''

import socket, time, sndRcdFtrX

serverIP = '***.***.***.***'
ml_port = 7777

try:
	ml_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
	ml_soc.connect((serverIP,ml_port))
	while (True):
		time.sleep(10)
		try:
			ml_value=str(sndRcdFtrX.main())
			ml_soc.send(ml_value)
		except:
			ml_soc.close()
			break	
	
except KeyboardInterrupt:
	print 'exit now'
	ml_soc.close()
	exit()
