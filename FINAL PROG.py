# -*- coding: utf-8 -*-
from __future__ import division

import os
from gps import *
from time import *
from math import *
import picamera
import time
import threading
rTerre=6378137
nbrEssais=50
camera=picamera.PiCamera()
gpsd = None

class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd
        gpsd=gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = True
    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next()
if __name__ == '__main__':
    gpsp = GpsPoller()
    try:
        gpsp.start()
        latDepart=0
        longDepart=0
        while True:
            
            os.system('clear')
            print 'gps reading'
            print '-------------------------------'
            print 'latitude' , gpsd.fix.latitude
            print 'longitude' , gpsd.fix.longitude
                        
            try :
                listNouvLong,listNouvLat,listNouvLongTri,listNouvLatTri=[],[],[],[]
                nbrLong,nbrLat=[],[]
                for k in range(nbrEssais): # Lancement acquisition des données à trier
                    listNouvLong.append(gpsd.fix.longitude)
                    listNouvLat.append(gpsd.fix.latitude)
                    time.sleep(1/nbrEssais)

                listNouvLongTri=list(set(listNouvLong)) #enlève les doublon
                listNouvLatTri=list(set(listNouvLat))

                '''print(listNouvLongTri)
                print(listNouvLatTri)'''
                

                for i in listNouvLongTri:
                    nbrLong.append(listNouvLong.count(i))

                for i in listNouvLatTri:
                    nbrLat.append(listNouvLat.count(i))

                '''print(nbrLat)
                print(nbrLong)'''

                longArrivee=listNouvLongTri[nbrLong.index(max(nbrLong))]
                latArrivee=listNouvLatTri[nbrLat.index(max(nbrLat))]


               

                '''arc=acos(sin(latDepart)*sin(latArrivee)+cos(latDepart)*cos(latArrivee)*cos(longArrivee-longDepart))
                distance=arc*rTerre'''
                distance=sqrt((rTerre*((latDepart-latArrivee)))**2+((rTerre*sin(pi/2-latDepart)*(longDepart-longArrivee))**2))
                print(distance)

                if distance > 10 :
                    camera.capture('pict_longi_'+str(longArrivee) + '_lati_'+ str(latArrivee)+'_.jpg')
                    print('photo')
                    latDepart=latArrivee
                    longDepart=longArrivee

                else:
                    pass
                
                
            except:
                pass
    except:
        pass
