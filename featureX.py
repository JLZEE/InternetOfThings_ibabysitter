'''
Columbia university, iot project

This code is used to extract all 160 features from dataset
'Baby_sound' file contains all baby crying sound, you can build one by yourself, all audio file should be .wav
'City_sound' file contains all city noise sound, you can build one by yourself, all audio file should be .wav
All features will be saved in 'csvfeat.csv' file
Using this feature matrix, you can train a machine learning model for baby crying prediction 
'''

import numpy as np
import csv
import test_featureAPI
from os import walk

def main():

	writer = csv.writer(file('csvfeat.csv', 'wb'))

	# write title
	firstRow = []
	for i in range(0, 160):
		firstRow.append('feature{0}'.format(i))
	firstRow.append('label')
	writer.writerow(firstRow)
	#print len(firstRow)
	
	# write city features
	file_names = []
	
	for (dirpath, dirnames, filenames) in walk('City_Sound/'):
		file_names.extend(filenames)

	file_names.sort()

	print "load city sound..."
	
	for i in range(0,len(file_names)):
		try:
			mrg_feat0 = test_featureAPI.merge_features("City_Sound/" + file_names[i])
			#mrg_feat0 = np.append(mrg_feat0, [0])
			mrg_feat00 = mrg_feat0.tolist()
			mrg_feat00.append(0)
			writer.writerow(mrg_feat00)
			#print np.shape(mrg_feat0)
			#print mrg_feat0
		except:
			print "loading", ("City_Sound/"+ file_names[i]), "failed"
	
	# write baby features
	file_names2 = []
	
	for (dirpath, dirnames, filenames) in walk('Baby_Sound/'):
		file_names2.extend(filenames)

	file_names2.sort()

	print "load baby sound..."

	for i in range(0,len(file_names2)):
		#print "Baby_Sound/" + file_names2[i]
		try:
			mrg_feat1 = test_featureAPI.merge_features("Baby_Sound/" + file_names2[i])
			#mrg_feat1 = np.append(mrg_feat1, [1])
			mrg_feat11 = mrg_feat1.tolist()
			mrg_feat11.append(1)
			writer.writerow(mrg_feat11)
			#print np.shape(mrg_feat1)
			#print mrg_feat1
		except:
			print "loading" , ("Baby_Sound/"+ file_names2[i]), "failed"
	

if __name__ == '__main__':
	main()
