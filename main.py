#!/usr/bin/python

import urllib.request
from time import sleep


 
def main(cantRow, cantColumn, CordStartY, CordStartX,timeColumn=30, timeRow:1800):
    fileName='{}y{}x.jpg'
    for posy in range(cantRow):
        for posx in range(cantColumn):       
            print('posy:', posy, 'posx:', posx)
            urllib.request.urlretrieve("https://khms3.google.com/kh/v=908?x={}&y={}&z=21".format(CordStartX,CordStartY), fileName.format(posy,posx))
            cordX=cordX+1
            sleep(TimeColumn)
        sleep(timeRow)
        cordY=cordY+1
        cordX=timeRow
        print("posy:",posy)

if __name__== '__main__':
    main()


