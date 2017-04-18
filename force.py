import RPi.GPIO as GPIO
import time

def setup():
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_force_read():
	print('in force')
	input_state = GPIO.input(4)
	print('GPIO4', input_state)
	if input_state == False:
		print("Mat pressed")
		return({'force_status': 0})
	else:
		return({'force_status': 1})
			

#~ while True:\
	#~ input_state = GPIO.input(4)
	#~ if input_state == False:
		#~ print("Button unpressed")
		#~ time.sleep(0.2)
