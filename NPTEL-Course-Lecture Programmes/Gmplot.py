# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:21:29 2021

@author: Lakhan Kumawat
"""
#20.6134567,72.9431185,87
import csv
from gmplot import gmplot


gmap = gmplot.GoogleMapPlotter(20.613456, 72.9431185,17)
#gmap.coloricon="https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png"

with open('LatLong.csv','r') as f:
    reader=csv.reader(f)
    k=0
    for row in reader:
        lat=float(row[0])
        long=float(row[1])
        
        if k==0:
            gmap.marker(lat, long, 'green')
            k=1
        else:
            gmap.marker(lat,long,'blue')
        
gmap.marker(lat,long,'red')
gmap.draw("Myhouse.html")