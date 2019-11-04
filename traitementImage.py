from PIL import Image
import random

im=Image.open('test.png')
#print(im.size)
#im.getpixel(i,j)
#im.putpixel((i,j),(r,g,b))
#im.save('test1.png')
for i in range(im.size[0]):
    for j in range(im.size[1]):
        '''r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)'''
        im.putpixel((i,j),(60,210,60))
        
im.save('test1.png')
print('ok')
        
im=Image.open('test1.png') 
#print(im.size)
#im.getpixel(i,j)
#im.putpixel((i,j),(r,g,b))
#im.save('test1.png')
a=0
nbrpix=im.size[0]*im.size[1]
for i in range(im.size[0]):
    for j in range(im.size[1]):
        if (im.getpixel((i,j)))[0]<70 and (im.getpixel((i,j)))[1]>200 and (im.getpixel((i,j)))[2]<70:
            a+=1
        else:
            pass
if a/nbrpix > 0.05:
    print('mauvaise herbe')
else:
    print('pas de mauvaise herbe')

print('ok')
