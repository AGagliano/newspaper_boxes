import RPi.GPIO as GPIO
import time






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
	
if __name__ == "__main__":
	GPIO.setmode(GPIO.BCM)

	GPIO_TRIGGER1 = 19
	GPIO_ECHO1 = 26
	GPIO_TRIGGER2 = 16
	GPIO_ECHO2 = 20
	
	GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
	GPIO.setup(GPIO_ECHO1, GPIO.IN)
	GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
	GPIO.setup(GPIO_ECHO2, GPIO.IN)
	
	try: 
		while True:
			dist1 = distance(GPIO_TRIGGER1, GPIO_ECHO1)
			print("Measured distance1 = %.1f cm" % dist1)
			dist2 = distance(GPIO_TRIGGER2, GPIO_ECHO2)
			print("Measured distance2 = %.f cm" % dist2)
			time.sleep(1)
	
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()
