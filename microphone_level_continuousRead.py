#!/usr/bin/python

import alsaaudio, time, audioop

card = 'sysdefault:CARD=Microphone'
inp=alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

inp.setperiodsize(160)

while True:
	#print('in while')
	l, data = inp.read()
	if l:
		print(audioop.max(data, 2))
	time.sleep(.001)
