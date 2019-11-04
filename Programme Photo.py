# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 13:49:03 2016

@author: ZIMMEJoan
"""


'''Activer la caméra'''############################################################################

#sudo raspi-config


'''Installation'''#################################################################################

#sudo apt-get update
#sudo apt-get install python-picamera


'''Réglages'''#####################################################################################

'''
camera.brightness = 70
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)
'''





'''Programme'''####################################################################################



import picamera


camera = picamera.PiCamera( )   #création d'une instance de la classe PiCamera


camera.capture('image.jpg')      #prendre une photo

































