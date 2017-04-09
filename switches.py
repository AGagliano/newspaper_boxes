#!/usr/bin/python
#
#switch_count.py
#
#Open up GPIO pins for limit switch for Door A and Door B on newspaper boxes
#Read in the most recent Door A and Door B open counts from txt file
#Add to the total count
#Write to the txt file the total count
###############################################################################

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

def run():
	GPIO.setup(26, GPIO.IN)
	#GPIO.setup(XXXX, GPIO.IN) #b door GPIO pin
	
	a_open = 0 #door starts closed
	b_open = 0 #door starts closed
	
	with open("Counts/door_count.txt", "r") as f:
		counts = f.readlines()
		a_count = int(counts[0])
		b_count = int(counts[1])
	
	#Can add in more nuance to counting the doors by day or to csv
	
	try:
		while True:
			a_input = GPIO.input(26)
			# b_input = GPIO.input(XXXX)
			
			#detect when door opens, and add a count
			if a_input != a_open:
				a_open = abs(a_open - 1)
				if a_open == 1:
					a_count += 1 
					print("Door A opened. Count: ", a_count)
				else: 
					print("Door A closed.")
		
			#if b_input != b_open:
				#b_open = abs(b_open - 1)
				#if b_open == 1:
					#b_count += 1
					#print("Door B opened. Count: ", b_count)
			time.sleep(0.2)
	
	except KeyboardInterrupt:
		with open("Counts/door_count.txt", "w") as f:
			f.write(str(a_count)+"\r\n")
			f.write(str(b_count)+"\r\n")

if __name__ =="__main__":
	run()

