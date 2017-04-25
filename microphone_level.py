#!/usr/bin/python

import alsaaudio, time, audioop

def setup():
	print('in setup function')
	card = 'sysdefault:CARD=Microphone'
	print('changed card')
	inp=alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)
	print('set inp, alsaasuio')
	
	inp.setchannels(1)
	inp.setrate(8000)
	inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

	inp.setperiodsize(160)
	print('about to leave setup')
	return inp

#~ while True:
	#~ l, data = inp.read()
	#~ if l:
		#~ print(audioop.max(data, 2))
	#~ time.sleep(.001)

def get_sound(inp):
	#print('in get_sound function')
	while True:
		#print('in while loop')
		l, data = inp.read()
		if l>0:
			val = audioop.max(data, 2)
			return({'sound': val})
		time.sleep(0.001)

if __name__ == "__main__":
	setup()
	get_sound()
