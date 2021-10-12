#!/usr/bin/python
import argparse
import urllib.request
from time import sleep
import sys

def main(CoordStartX:int, CoordStartY:int,CoordEndX:int,CoordEndY:int,zoom:int,timeBetweenReq:int, timeBetweenBatches:int):
    fileName='{}y{}x.jpg'
    for posy in range(CoordStartY,CoordEndY):
        for posx in range(CoordStartX, CoordEndX):       
            print('posy:', posy, 'posx:', posx)
            urllib.request.urlretrieve("https://khms3.google.com/kh/v=908?x={}&y={}&z={}".format(posx,posy, zoom), fileName.format(posy,posx))
            sleep(timeBetweenReq)
        sleep(timeBetweenBatches)
        print("posy:",posy)

if __name__== '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-tr', '--timeBetweenRequests',type=int, help='time between requests <in second>', default=30)
    parser.add_argument('-tb', '--timeBetweenBatches',type=int, help='time between batches <in second>', default=1800)
    parser.add_argument('-z', '--zoom',type=int, help='level zoom <numbre from 1 to 21>')   
    parser.add_argument('-c', '-coord',type=int, nargs=4,help='Coordiantes <StartX, StartY, EndX, EndY>')
    args = parser.parse_args()
    try:
        main(args.c[0], args.c[1], args.c[2],  args.c[3], args.zoom, args.timeBetweenRequests, args.timeBetweenBatches)
    except urllib.error.URLError as e:
        raise Excetion(e)



