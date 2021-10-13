import cv2 as cv
import qrcode
from PIL import Image, ImageDraw
from pyzbar import pyzbar
import sys


with Image.open(sys.argv[1]) as im:
    found = False
    a = 0.5
    b = 0.5
    for _ in range(20):
        #print(a,b)
        draw = ImageDraw.Draw(im)
        draw.rectangle([int(a*im.size[0]),int(a*im.size[1]),int(b*im.size[0]),int(b*im.size[1])], fill='white')
        try:
            if pyzbar.decode(im)==[]:
                a-=0.02
                b+=0.02
                continue
            else:    
                found = True
                print(str(pyzbar.decode(im)))
                print()
                print(str(pyzbar.decode(im)[0]).split("data=b'")[1].split("',")[0])
                print()
                break
        except:
            pass
if not found:
    print("Was not able to extract QR-data from image")

