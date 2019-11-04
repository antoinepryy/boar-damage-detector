# -*- coding: utf-8 -*-
from math import *
from numpy import *
rTerre=6378137
longi1=6.158643167
longi2=6.158643167
lati1=49.097237164
lati2=49.097200000

    

arc=acos(sin(lati1)*sin(lati2)+cos(lati1)*cos(lati2)*cos(longi1-longi2))
distance1=arc*rTerre

distance2=sqrt((rTerre*((lati1-lati2)))**2+((rTerre*sin(pi/2-lati1)*(longi2-longi1))**2))

print(distance1)
print(distance2)

