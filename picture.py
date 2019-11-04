import picamera
import time



camera=picamera.PiCamera()
longArrivee=2
latArrivee=3

'''camera.capture('pict_longi_'+str(longArrivee) + '_lati_'+ str(latArrivee)+'_.jpg')'''

try:
    camera.start_preview()
    time.sleep(20)
    camera.stop_preview()
finally:
    camera.close()
    

'''camera.start_preview()
try:
    for i in range(100):
        camera.saturation=i
        time.sleep(0.2)
finally:
    camera.stop_preview()'''
    
