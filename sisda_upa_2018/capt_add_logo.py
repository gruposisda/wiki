#!/usr/bin/python

from time import sleep
from datetime import datetime
from picamera import PiCamera
from PIL import Image

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

img_base_name = './out/image_{}-{}.jpg'

def cap_images(exposure_mode,name,gain,n=1):
    for i in range(n):
        print('capturando imagem com ganho {}'.format(gain))
        sleep(0.2)
        camera.capture(name.format(now.hour,now.minute))
    return;


cap_images(exposure_mode="auto",name=img_base_name,gain="auto",n = 1)

#add logo
hour = now.hour
minute = now.minute
img_base_name = './out/image_{}-{}.jpg'
input_image = img_base_name.format(str(hour),str(minute))


photo = Image.open(input_image)
logo = Image.open('logos/logos_red.png')
photo.paste(logo,(2208,2150))

output_image = './out/image_{}-{}.'
output_image = output_image.format(str(hour),str(minute))+'_logo.jpg'
photo.save(output_image)
