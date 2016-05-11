'''
Columbia university iot project

this program is used to use the feature extraction API
you need to install python_speech_features first
http://python-speech-features.readthedocs.io/en/latest/
'''


import numpy as np
import scipy
from features import mfcc, logfbank, fbank, ssc
import scipy.io.wavfile as wav

'''
feature extraction:
1st feature mfcc, output mfcc_feat is [frame_num, 13] matrix
each row holds 1 feature vector of a frame

2nd feature logfbank, output logfbank_feat is [frame_num, 26] matrix
each row holds 1 feature vector of a frame

3rd feature fbank,
output fbank_feat1 is [frame_num, 26] matrix, samiliar to logfbak_feat
output fbank_feat2 is [frame_num, ] matrix, each row holds the energy of
every frame

4th feature ssc, output ssc_feat is [frame_num, 26] matrix
each row holds 1 feature vector of a frame
'''
'''
(rate,sig) = wav.read("cupsonly.wav")

mfcc_feat = mfcc(sig,rate)
logfbank_feat = logfbank(sig,rate)
[fbank_feat1, fbank_feat2] = fbank(sig,rate)
ssc_feat = ssc(sig,rate)
'''
def mfcc_feature(sig,rate):
    '''
    this function is used to change the mfcc_feat of every frame into a 
    statistic value of a piece of audio

    output features including:
    1. average of every 13 features in all frames
    2. maximum of every 13 features in all frames
    3. minimum of every 13 features in all frames
    4. varience of every 13 features in all frames

    INPUT: mfcc_feat (FRAMENUM, 13)
    OUTPUT: ave_mfcc (13, )
    		max_mfcc (13, )
    		min_mfcc (13, )
    		var_mfcc (13, )
    '''
    mfcc_feat = mfcc(sig,rate)
    ave_mfcc = np.mean(mfcc_feat, axis = 0)
    max_mfcc = np.max(mfcc_feat, axis = 0)
    min_mfcc = np.min(mfcc_feat, axis = 0)
    var_mfcc = np.var(mfcc_feat, axis = 0)

    return [ave_mfcc, max_mfcc, min_mfcc, var_mfcc]

def logfbank_feature(sig,rate):
	'''
	this function is used to change the logfbank_feature of every frame into
	statistic value

	output features including:
	1. average of 26 features
	2. maximum ...
	3. minimum ...
	4. varience ...

	INPUT: logfbank_feat (FRAMENUM, 26)
	OUTPUT: ave_logfbank (26, )
			max_logfbank (26, )
			min_logfbank (26, )
			var_logfbank (26, )
	'''
	logfbank_feat = logfbank(sig,rate)
	ave_logfbank = np.mean(logfbank_feat, axis = 0)
	max_logfbank = np.max(logfbank_feat, axis = 0)
	min_logfbank = np.min(logfbank_feat, axis = 0)
	var_logfbank = np.var(logfbank_feat, axis = 0)

	return [ave_logfbank, max_logfbank, min_logfbank, var_logfbank]

def energy_feature(sig,rate):
	'''
	this function is used to get the statistic energy value

	output features including:
	1. log of average energy of all frames
	2. log of maximum ...
	3. log of minimum ...
	4. log of varience ...
	
	INPUT: fbank_feat2 (FRAMENUM, )
	OUTPUT: ave_energy(1, )
			max_energy(1, )
			min_energy(1, )
			var_energy(1, )
	'''
	[fbank_feat1, fbank_feat2] = fbank(sig,rate)
	ave_energy = np.log(np.mean(fbank_feat2))
	max_energy = np.log(np.max(fbank_feat2))
	min_energy = np.log(np.min(fbank_feat2))
	var_energy = np.log(np.var(fbank_feat2))

	return [ave_energy, max_energy, min_energy, var_energy]

def ssc_feature(sig,rate):
	'''
	this function is used to get the statistic ssc value

	output features including:
	1. average of 26 features
	2. maximum ...
	3. minimum ...
	4. varience ...

	INPUT: ssc_feat (FRAMENUM, 26)
	OUTPUT: ave_ssc (26, )
			max_ssc (26, )
			min_ssc (26, )
			var_ssc (26, )
	'''
	ssc_feat = ssc(sig,rate)
	ave_ssc = np.mean(ssc_feat, axis = 0)
	max_ssc = np.max(ssc_feat, axis = 0)
	min_ssc = np.min(ssc_feat, axis = 0)
	var_ssc = np.var(ssc_feat, axis = 0)

	return [ave_ssc, max_ssc, min_ssc, var_ssc]

def merge_features(fileName):
	'''
	this function is used to merge all features together
	INPUT: all frame based features
	OUTPUT: mrg_feat (264, )
	'''
	(rate,sig) = wav.read(fileName)
	mfcc_result = mfcc_feature(sig,rate)
	logfbank_result = logfbank_feature(sig,rate)
	energy_result = energy_feature(sig,rate)
	ssc_result = ssc_feature(sig,rate)

	#mrg_feat = np.append(np.append(mfcc_result, logfbank_result),np.append(energy_result, ssc_result))
	mrg_feat = np.append(mfcc_result,np.append(energy_result, ssc_result))

	return mrg_feat


#print fbank_feat[1:3,:]
'''
print 'mfcc shape', np.shape(mfcc_feat)
print 'logfbank shape', np.shape(logfbank_feat)
print 'fbank_feat1 shape', np.shape(fbank_feat1)
print 'fbank_feat2 shape', np.shape(fbank_feat2)
print 'ssc shape', np.shape(ssc_feat)

print 'mfcc: ', mfcc_feature(mfcc_feat)
print 'logfbank: ', logfbank_feature(logfbank_feat)
print 'energy: ', energy_feature(fbank_feat2)
print 'ssc: ', ssc_feature(ssc_feat)
'''
def main():
	mrg_feat = merge_features("cupsonly.wav")
	#mrg_feat = np.append(mrg_feat, [1])
	print np.shape(mrg_feat)
	print mrg_feat

if __name__ == '__main__':
	main()
