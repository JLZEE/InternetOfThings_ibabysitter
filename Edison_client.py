'''
This code is used for Edison client, it will sense the temperature every few seconds
and then send the temperature message to the EC2 server.
Another function of this part is operating 'open fan' command from server.
'''

import socket, TempDis, Open_fan, time
import threading

ExitFlag = True
temp_value_float = 25.0

def recv_command(serverIP):
	global ExitFlag
	global temp_value_float
	recv_command_port = 8888
	recv_command_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	recv_command_soc.connect((serverIP,recv_command_port))
	while (ExitFlag):
		command_from_server = recv_command_soc.recv(1024)
		op_flag = True
		if (temp_value_float >= 20.0):
			Open_fan.level_1()
		else:
			Open_fan.level_0()
		print "Open fan command received!"


def send_temp(serverIP):
	global ExitFlag
	global temp_value_float
	temp_port = 6666
	temp_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	temp_soc.connect((serverIP,temp_port))
	while (ExitFlag):
		time.sleep(10)
		temp_value = TempDis.main()
		temp_value_float = float(temp_value)
		temp_soc.send(temp_value)

if __name__ == "__main__":
	ExitFlag = True
	try:
		global serverIP
		global op_flag
		serverIP = '***.***.***.***'
		op_flag = False

		receive_command = threading.Thread(target = recv_command, args = (serverIP,))
		receive_command.start()

		send_temperature = threading.Thread(target = send_temp, args = (serverIP,))
		send_temperature.start()
	except KeyboardInterrupt:
		ExitFlag = False
		exit
