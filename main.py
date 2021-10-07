#!/usr/bin/python

import urllib.request
from time import sleep
import sys

def main(CoordStartX, CoordStartY,CoordEndX,CoordEndY,timeBetweenReq=30, timeBetweenBatches=1800, zoom:int):
    fileName='{}y{}x.jpg'
    for posy in range(CordStartY,CordEndY):
        for posx in range(CordStartX, CordEndX):       
            print('posy:', posy, 'posx:', posx)
            urllib.request.urlretrieve("https://khms3.google.com/kh/v=908?x={}&y={}&z={}".format(posx,posy, zoom), fileName.format(posy,posx))
            sleep(timeBetweenReq)
        sleep(timeBetweenBatches)
        print("posy:",posy)

if __name__== '__main__':
    args=sys.argv()
        
    main()


