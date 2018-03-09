#!/usr/bin/env python

import picamera
import time

cam = picamera.PiCamera()
cam.start_preview()
time.sleep(60)
#cam.start_preview(fullscreen=False, window=(200, -400, 1200, 1600))
#time.sleep(5)
cam.stop_preview()
cam.close()

