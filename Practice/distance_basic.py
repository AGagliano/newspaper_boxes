#!/usr/bin/python
#
# ultrasonic_distance_basic.py
# Measure distance using an two ultrasonic modules (HC-SR04)
# and play audio file in response
#
# Code largerly adapted from:
# http://www.raspberrypi-spy.co.uk/tag/ultrasonic/
# Author : Matt Hawkins
# Date   : 16/10/2016
# -----------------------

# Import required Python libraries
from __future__ import print_function
import time
import RPi.GPIO as GPIO
import pygame

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER1 = 19 #output
GPIO_ECHO1    = 26 #input
GPIO_TRIGGER2 = 16 #output
GPIO_ECHO2    = 20 #input

# Set distance range to trigger sound
dist_range = 10 #in cm

def init_ultrasonic(GPIO_TRIGGER, GPIO_ECHO):
	# Set pins as output and input
	GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
	GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

	# Set trigger to False (Low)
	GPIO.output(GPIO_TRIGGER, False)
	
	# Allow module to settle
	print("Allowing sensor to settle")
	time.sleep(0.5) 

def get_dist(GPIO_TRIGGER, GPIO_ECHO):
	# Send 10us pulse to trigger
	GPIO.output(GPIO_TRIGGER, True)
	# Wait 10us
	#time.sleep(0.00001)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	start = time.time()	
	count = 0

	while GPIO.input(GPIO_ECHO)==0:
		print('echo is 0')
		start = time.time()
		count += 1
	  #~ if count > 1000:
                  #~ break

	while GPIO.input(GPIO_ECHO)==1:
		print('echo is 1')
		stop = time.time()

	
	
	
	
	  
	# Calculate pulse length
	elapsed = stop-start 
	
	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound in cm/halved
	distance = elapsed * 17150  

	# That was the distance there and back so halve the value
	distance = distance / 2
	
	print("Distance : {0:5.1f}".format(distance))

	return distance
	
		
def run(): 
	init_ultrasonic(GPIO_TRIGGER1, GPIO_ECHO1)
	#init_ultrasonic(GPIO_TRIGGER2, GPIO_ECHO2)

        count=0
	while True:
		print("Distance1")
		distance1 = get_dist(GPIO_TRIGGER1, GPIO_ECHO1)
		#print("Distance2")
		#distance2 = get_dist(GPIO_TRIGGER2, GPIO_ECHO2)
		count+= 1
		print('Count: ' , count)

	# Reset GPIO settings
	GPIO.cleanup()  
	

if __name__ == "__main__":
	run()
