'''
This file is used to make baby crying detection by using AWS ML
'''

import base64
import boto3
import json
import os
import sys
import time,random

# aws.py saves aws account information
import aws

import record
sys.path.insert(0, '/home/pi/Desktop/****')
import numpy as np
import csv
import test_featureAPI

def main():
	'''
	NOTICE:
	may need to change PredictEndpoint value
	'''

	record.main()
	'''
	writer = csv.writer(file('soundRcd.csv', 'wb'))

	# write title
	firstRow = []
	for i in range(0, 160):
		firstRow.append('feature{0}'.format(i))
	firstRow.append('label')
	writer.writerow(firstRow)
	#print len(firstRow)
	'''
	# write city features
	file_names = 'file.wav'
	
	mrg_feat = test_featureAPI.merge_features(file_names)
	mrg_feat_rcv = mrg_feat.tolist()
	#mrg_feat_rcv.append(0)
	#writer.writerow(mrg_feat_rcv)
	ml = aws.getClient('machinelearning','us-east-1')
	attributeStr={}
	for i in range(0, 159):
		attributeStr['feature{0}'.format(i)] = '{0}'.format(mrg_feat_rcv[i])

	print 'perdicting...'

	response = ml.predict(
	    MLModelId='**********', 
	    Record=attributeStr,
	    PredictEndpoint='**********'
	)
	print response['Prediction']['predictedLabel']
	
	return response['Prediction']['predictedLabel']
	
if __name__ == '__main__':
	print main()




