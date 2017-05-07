import RPi.GPIO as GPIO
import time
import pygame
import force
import sys
import random


def distance(GPIO_TRIGGER, GPIO_ECHO):
	GPIO.output(GPIO_TRIGGER, True)
	
	time.sleep(.00001)
	GPIO.output(GPIO_TRIGGER, False)
	
	StartTime = time.time()
	StopTime = time.time()
	
	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()
		
	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
		
	TimeElapsed = StopTime - StartTime
	distance = (TimeElapsed * 34300) / 2
	
	return distance

def play(audio_file):
	pygame.mixer.init()
	pygame.mixer.music.load(audio_file)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True: #don't return until audio is finished
		continue
		
def run(print_bool, experience):
	GPIO.setmode(GPIO.BCM)

	GPIO_TRIGGER1 = 19
	GPIO_ECHO1 = 26
	GPIO_TRIGGER2 = 16
	GPIO_ECHO2 = 20
	
	GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
	GPIO.setup(GPIO_ECHO1, GPIO.IN)
	GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
	GPIO.setup(GPIO_ECHO2, GPIO.IN)

	count = 0
	
	if print_bool == True:
		print('proximity sensor pins set up')

	force.setup()
	
	if print_bool == True:
		print('force pins setup')	

	dist_thresh1 = 50 #Anything less than 1 m away and the extra extra sound will play
	dist_thresh2 = 50
	
	#with open('distance_printout.txt', 'w') as f:
	try: 
		while True:
			force_val_dict = force.get_force_read()
			if print_bool == True:
				print('Just finished force read function')
			force_val = force_val_dict['force_status']
			#f.write("force value: %.f \n" % force_val)
			#If no one is standing on mat, detect distance and play audio accordingly
			if force_val != 1:
				count = 0
				dist1 = distance(GPIO_TRIGGER1, GPIO_ECHO1)
				if print_bool == True:
					print("Measured distance1 = %.1f cm" % dist1)
				#f.write("Measured distance1 = %.1f cm\n" % dist1)
				dist2 = distance(GPIO_TRIGGER2, GPIO_ECHO2)
				if print_bool == True:
					print("Measured distance2 = %.1f cm" % dist2)
				#f.write("Measured distance2 = %.1f cm\n" % dist2)
				
				
				if dist1 < dist_thresh1 or dist2 < dist_thresh2:
					if print_bool == True:
						print('Play extra extra audio')
					#f.write("play audio\n")
					play("Audio/extra_extra_short.mp3")
			#Add to the count that the person is still standing on the mat
			else: 
				count += 1
				#box as monitor experience
				if experience == 1:
					if print_bool == True:
						print('Count: ', count)
					if count == 20: #I'll need to massage this threshold tomorrow
						play("Audio/loitering1.mp3")
						if print_bool == True:
							print('Playing the you have been loitering message')
					if count == 60: #I'll need to massage this threshold tomorrow
						play("Audio/stop_loitering_too_long.mp3")  #######mp3 file to be added
						if print_bool == True:
							print('Playing the youve been here too long loitering message')
					if count == 90: #I'll need to massage this threshold tomorrow
						play("Audio/still_loitering_police.mp3")  #######mp3 file to be added
						if print_bool == True:
							print('Playing the cops are coming message')

				#box as assistant experience
				if experience == 2:
					if print_bool == True:
						print('Count: ', count)
					if count == 20: #I'll need to massage this threshold tomorrow
						play("Audio/homeless_on_shattuck.mp3")  ######mp3 file to be added
						if print_bool == True:
							print('Playing suggesting food for homeless audio')

				#box as researcher experience
				if experience == 3:
					if print_bool == True:
						print('Count: ', count)
					if count == 20: #I'll need to massage this threshold tomorrow
						play("Audio/loitering1.mp3") ######put in mp3 file
						if print_bool == True:
							print('Playing the what do you think about me message')
					if count == 60: #I'll need to massage this threshold tomorrow
						play("Audio/loitering1.mp3")  #######mp3 file to be added
						if print_bool == True:
							print('Playing the how do you think I collect data message')
			
			time.sleep(1)
			
	
	except KeyboardInterrupt:
		#print("Measurement stopped by User")
		GPIO.cleanup()

	
	
if __name__ == "__main__":
	try:
		print_bool = sys.argv[1]  #on system run, type true or false boolean (True or False)
		experience = sys.argv[2]  #on system run, type 1, 2, or 3 for different experiences, or leave blank for random.
	except:
		print_bool = False
		experience = random.randint(1, 3)
	if print_bool == 'True':
		print_bool = True
	print('print boolean: ' + str(print_bool))
	print('experience: ' + str(experience))
	run(print_bool, experience)
	
