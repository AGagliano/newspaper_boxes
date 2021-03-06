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
import force

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
	time.sleep(0.0001)
	GPIO.output(GPIO_TRIGGER, False)
	start = time.time()
	
	while GPIO.input(GPIO_ECHO)==0:
          print('Echo is 0')
	  start = time.time()
	
	while GPIO.input(GPIO_ECHO)==1:
          print('Echo is 1')
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
	
	
def play(audio_file):
	pygame.mixer.init()
	pygame.mixer.music.load(audio_file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True: #don't return until audio is finished
		continue
		
def run(): 
	init_ultrasonic(GPIO_TRIGGER1, GPIO_ECHO1)
	init_ultrasonic(GPIO_TRIGGER2, GPIO_ECHO2)
	force.setup()

	while True:
		print("Distance1")
		distance1 = get_dist(GPIO_TRIGGER1, GPIO_ECHO1)
		print("Distance2")
		distance2 = get_dist(GPIO_TRIGGER2, GPIO_ECHO2)
		if distance1 < dist_range or distance2 < dist_range:
			force_val_dict = force.get_force_read()
			force_val = force_val_dict['force_status']
			print('got force value')
			if force_val == 0:   #If no one is standing on the mat, then okay to sound the audio
                                print('start playing audio')
				play("Audio/extra_extra_short.mp3")
				print('stop playing audio')

	# Reset GPIO settings
	GPIO.cleanup()  
	

if __name__ == "__main__":
	run()
