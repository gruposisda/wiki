#!/usr/bin/python

from time import sleep
from datetime import datetime
from picamera import PiCamera

try:
    camera = PiCamera(resolution=(3280, 2464), framerate=6)
except:
    camera = camera

now = datetime.now()

#configure camera
camera.awb_gains = (1, 1)
camera.awb_mode = 'off'
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0

img_base_name = './out/image_{}{}_g{}_{}.jpg'

def cap_images(exposure_mode,name,gain,n=3):
    for i in range(n):
        print('capturando imagem {} com ganho {}'.format(i,gain))
        sleep(0.2)
        camera.capture(name.format(now.month,now.day,gain,i))
    return;


cap_images(exposure_mode="auto",name=img_base_name,gain="auto",n = 1)