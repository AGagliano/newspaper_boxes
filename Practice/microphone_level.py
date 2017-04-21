#!/usr/bin/python

import alsaaudio, time, audioop

def setup():
	inp=alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

	inp.setchannels(1)
	inp.setrate(8000)
	inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

	inp.setperiodsize(160)
	return inp

#~ while True:
	#~ l, data = inp.read()
	#~ if l:
		#~ print(audioop.max(data, 2))
	#~ time.sleep(.001)

def get_sound(inp):
	while True:
		l, data = inp.read()
		if l>0:
			val = audioop.max(data, 2)
			return({'sound': val})
		time.sleep(0.001)
