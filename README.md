# InternetOfThings_ibabysitter

This is a Columbia University IoT project - ibabysitter, please visit our website for more information:
http://i-babysitter.weebly.com

The code is basically divided into 4 parts:
1. Server on EC2
2. Client part on Intel Edison
3. Client part on Raspberry Pi
4. Android App

## Server on EC2
A single code server.py is used in AWS EC2 server. The code at this part is simple - receiving and forwarding message between Intel Edison, Raspberry Pi and Android App

## Client part on Raspberry Pi
Includes BabyCry_client.py, record.py and sndRcdFtrX.py. record.py is for recording sound; sndRcdFtrX.py is for machine learning prediction and BabyCry_client.py is for sending message to EC2 server
