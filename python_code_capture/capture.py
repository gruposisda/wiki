#!/usr/bin/python

from time import sleep
from datetime import datetime
from picamera import PiCamera

camera = PiCamera(resolution=(3280, 2464), framerate=6)
now = datetime.now()
sleep(2)
camera.start_preview()
sleep(2)
camera.stop_preview()


sleep(2)
for i in range(2):
    print('capturando imagem automatica')
    sleep(0.2)
    camera.capture('./out/auto_{}{}_{}.jpg'.format(now.month, now.day, i)) 

camera.awb_gains = (1, 1)
camera.awb_mode = 'off'
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0

img_base_name = './out/image_{}{}_g{}_{}.jpg'


camera.exposure_mode = 'auto'
gain = 'auto'

sleep(2)
for i in range(2):
    print('capturando imagem {} com ganho {}'.format(i, gain))
    sleep(0.2)
    camera.capture(img_base_name.format(now.month, now.day, gain, i)) 


camera.exposure_mode = 'off'
gain = 10 
camera.ISO = gain

sleep(2)
for i in range(3):
    print('capturando imagem {} com ganho {}'.format(i, gain))
    sleep(0.2)
    camera.capture(img_base_name.format(now.month, now.day, gain, i)) 



gain = 60
camera.exposure_mode = 'off'
camera.ISO = gain
sleep(2)
for i in range(3):
    print('capturando imagem {} com ganho {}'.format(i, gain))
    sleep(0.2)
    camera.capture(img_base_name.format(now.month, now.day, gain, i)) 


gain = 100
camera.exposure_mode = 'off'
camera.ISO = gain

sleep(2)
for i in range(3):
    print('capturando imagem {} com ganho {}'.format(i, gain))
    sleep(0.2)
    camera.capture(img_base_name.format(now.month, now.day, gain, i)) 
