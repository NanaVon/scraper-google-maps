#!/usr/bin/python

import urllib.request
from time import sleep
import sys

def main(cantRow, CordStartY, CordStartX,CordEndY,CordEndX,timeColumn=30, timeRow:1800):
    fileName='{}y{}x.jpg'
    for posy in range(CordStartY,CordEndY):
        for posx in range(CordStartX, CordEndX):       
            print('posy:', posy, 'posx:', posx)
            urllib.request.urlretrieve("https://khms3.google.com/kh/v=908?x={}&y={}&z=21".format(posx,posy), fileName.format(posy,posx))
            sleep(TimeColumn)
        sleep(timeRow)
        print("posy:",posy)

if __name__== '__main__':
    args=sys.argv()
        
    main()


