import RPi.GPIO as GPIO
import time
import pygame
import force
import sys


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
		
def run(print_bool):
	GPIO.setmode(GPIO.BCM)

	GPIO_TRIGGER1 = 19
	GPIO_ECHO1 = 26
	GPIO_TRIGGER2 = 16
	GPIO_ECHO2 = 20
	
	GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
	GPIO.setup(GPIO_ECHO1, GPIO.IN)
	GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
	GPIO.setup(GPIO_ECHO2, GPIO.IN)
	
	if print_bool == True:
		print('proximity sensor pins set up')

		
	force.setup()
	
	if print_bool == True:
		print('force pins setup')	

	dist_thresh = 100 #Anything less than 1 m away and the extra extra sound will play
	
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
				dist1 = distance(GPIO_TRIGGER1, GPIO_ECHO1)
				if print_bool == True:
					print("Measured distance1 = %.1f cm" % dist1)
				#f.write("Measured distance1 = %.1f cm\n" % dist1)
				dist2 = distance(GPIO_TRIGGER2, GPIO_ECHO2)
				if print_bool == True:
					print("Measured distance2 = %.1f cm" % dist2)
				#f.write("Measured distance2 = %.1f cm\n" % dist2)
				
				
				if dist1 < dist_thresh or dist2 < dist_thresh:
					if print_bool == True:
						print('play audio')
					#f.write("play audio\n")
					play("Audio/extra_extra_short.mp3")
			
			
			time.sleep(1)
			
	
	except KeyboardInterrupt:
		#print("Measurement stopped by User")
		GPIO.cleanup()

	
	
if __name__ == "__main__":
	try:
		print_bool = sys.argv[1]  #on system run, type true or false boolean (True or False)
	except:
		print_bool = False
	if print_bool == 'True':
		print_bool = True
	print('print boolean: ' + str(print_bool))
	run(print_bool)
	
