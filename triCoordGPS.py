gpsp.start()
ancienneLat=gpsd.fix.latitude
ancienneLong=gpsd.fix.longitude
while True:
            
    os.system('clear')
    print 'gps reading'
    print '-------------------------------'
    print 'latitude' , gpsd.fix.latitude
    print 'longitude' , gpsd.fix.longitude
                        
    try :
         nouvelleLat=gpsd.fix.latitude
         nouvelleLong=gpsd.fix.longitude

         arc=acos(sin(ancienneLat)*sin(nouvelleLat)+cos(ancienneLat)*cos(nouvelleLat)*cos(nouvelleLong-ancienneLong))
         distance=arc*rTerre

        print(distance, "meters")

        ancienneLat=nouvelleLat
        ancienneLong=nouvelleLong

               
