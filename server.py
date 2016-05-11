'''
This code runs in EC2 server, receving and forwarding message 
between BabyCry_client, Edison_client and APP
'''

import boto.sns
import logging
import json,time,csv,sys
import aws

import socket
global open_fan_edison
open_fan_edison = -1
import threading
import time
global temp_now
temp_now = None
global ml_flag
ml_flag = -1


#Thread 1 -> receive Mobile APP msg
#Attention: don't forget to change the code in android, where we have deleted one more ccondition

class app_Function(threading.Thread):
  def run(self):
    global open_fan_edison
    global ml_flag
    app_serverPORT=5555
      while True:
        try:
          app_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          app_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
          app_soc.bind(('0.0.0.0',app_serverPORT))
          app_soc.listen(5)
          app_conn,app_addr = app_soc.accept()
          print 'New app connection'
          while True:
            try:
              app_conn.send("Ready"+'\r\n')
              app_conn.settimeout(2.0)
              app_msg1 = app_conn.recv(1024)
              app_conn.settimeout(None)
              if(app_msg1.find('OK') == -1):


              app_conn.close()
              break
            except socket.timeout:
              app_conn.close()
              break                                         
          if (int(ml_flag) ==1):
            snsResource = aws.getResource('sns', 'us-east-1')
            snsClient = aws.getClient('sns', 'us-east-1')
            subject_content = 'Alert! '
            message_content = subject_content
            topic = snsResource.Topic('**********')
            snsClient.publish(TopicArn='**********', Message=message_content, Subject=subject_content)


          alert_msg="Dangerous! Temperature Now is:"+str(temp_now)
          print ("Alert!!",alert_msg)
          app_conn.send(alert_msg+'\r\n')
          print "msg has been sent"
          app_msg2 = app_conn.recv(1024)
          appThread = threading.Lock()
          if appThread.acquire():
                  ml_flag = 0 #tempory 0 for one minute
                  appThread.release()
                  #If it can run to this sentence, it means that app has sent a msg, 
                  #Change here to open fan
          if (app_msg2.find('OPEN') == -1):
                  app_conn.close()
                  break
          open_fan_edison =1
          print ("change in ML in FAN FLAG", open_fan_edison)
          print ("Got connection from",app_addr)
          print (app_msg2)
        except:
          app_soc.close()
          app_conn.close()
          continue

#Thread 2 -> receive Temperature
class temp_Function(threading.Thread):
  def run(self):
    global temp_now
    temp_serverPORT = 6666
    while True:
      try:
        temp_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        temp_soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        temp_soc.bind(('0.0.0.0',temp_serverPORT))
        temp_soc.listen(5)
        temp_conn,temp_addr = temp_soc.accept()
        while True:
          temp_msg = temp_conn.recv(1024)
          temp_now = temp_msg
          print ("temp_now",temp_now)
      except:
          continue
#Thread 2''-> Send open fan to Edison
class openFan_Edison(threading.Thread):
  def run(self):
    global open_fan_edison
    openFan_Edison_Port = 8888
    while True:
      try:
        openFan_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        openFan_soc.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        openFan_soc.bind(('0.0.0.0',openFan_Edison_Port))
        openFan_soc.listen(1)
        openFan_conn,openFan_addr = openFan_soc.accept()
        while True:
          #print ("FAN FLGA!", open_fan_edison)
          if (open_fan_edison ==1):
            openFan_conn.send("Open Fan!")
            open_fan_edison = -1
      except:
          continue



#Thread 3 -> receive sound features
class ml_Function(threading.Thread):
  def run(self):
    global ml_flag
    ml_serverPORT = 7777
    while True:
      try:
        ml_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ml_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        ml_soc.bind(('0.0.0.0',ml_serverPORT))
        ml_soc.listen(5)
        ml_conn,ml_addr = ml_soc.accept()
        while True:
          ml_msg = ml_conn.recv(1024)
          mlThread = threading.Lock()
          if mlThread.acquire():
            ml_flag = ml_msg
            print ("ml_flag",ml_flag)
            mlThread.release()
      except:
        continue

if __name__ == '__main__':
  try:
    t1 = app_Function()
    t2 = temp_Function()
    t3 = ml_Function()
    t4 = openFan_Edison()
    try:
      t1.start()
      t2.start()
      t3.start()
      t4.start()
    except:
      "error: cannot set up threads"
  except KeyboardInterrupt:
    sys.exit()




