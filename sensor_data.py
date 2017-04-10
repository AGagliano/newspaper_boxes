#!/usr/bin/python

#####################################################################################

#Gets force (FSR) and sound intensity (microphone) sensor data.
#Returns the values in a dictionary form

#####################################################################################

from random import randint

def forceSensor():
	'''
	Gets and returns force sensor data
	'''
	val = randint(100, 199)  #Replace with Rasp. Pi code to get force sensor data
	return val

def soundSensor():
	'''
	Gets and returns sound intensity data
	'''
	val = randint(0, 10)  #Replace with Rasp. Pi code to get sound intensity decibels
	return val

def run():
	'''
	Puts sensor data into a dictionary and returns. 
	'''
	return {'force': forceSensor(), 'sound': soundSensor()}


if __name__ == '__main__':
    run()
