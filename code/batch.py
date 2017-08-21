#! /usr/bin/env python
#coding: utf-8

import sys
import numpy as np
import os
import draw_opt
import cv2
import re

def batch_processing():
	#--------------------------------------------------
	# load inputDate.txt
	#--------------------------------------------------
	try:
		with open('inputDate.txt','r') as f:
			date = f.readline().strip()
	except FileNotFoundError:
		print('Not Found: inputDate.txt')
		print('\tPlease soecify file directory in ./inputDate.txt')
		sys.exit(1)
	
	#-------------------------------------------------
	#processing all data
	#------------------------------------------------	
	direc = '/Volumes/HDD-IO/Tuna_conv/'+date
	fileList = os.listdir(direc)
	pattern = r'^(?!._).*(.mp4)$'
	repattern = re.compile(pattern)
	for file_name in fileList:
		if re.search(repattern,file_name):
			inputFile = direc + '/' + file_name
			draw_opt.main(inputFile)

if __name__ == '__main__':
	batch_processing()
