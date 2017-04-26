import RPi.GPIO as GPIO
import time
import sys

def setup():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_force_read():
	#print('in force function')
	input_state = GPIO.input(4)
	if input_state == 0:
		#print("Mat pressed")
		return({'force_status': 1})
	else:
		return({'force_status': 0})
			

#~ while True:\
	#~ input_state = GPIO.input(4)
	#~ if input_state == False:
		#~ print("Button unpressed")
		#~ time.sleep(0.2)
