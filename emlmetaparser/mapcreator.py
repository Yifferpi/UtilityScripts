#! /usr/bin/env python3

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv

def loadDB():
    data = open('data/data.csv', 'r')
    reader = csv.DictReader(data)
    l = dict()
    for row in reader:
        l[row['ip']] = row
    return l

def loadTraces():
    traces = open('data/traces.csv', 'r')
    reader = csv.reader(traces)
    l = list()
    for t in reader:
        print(type(t))
        l.append(t)
    return l

def createMap():
    m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
            llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    #m.fillcontinents(color='coral',lake_color='aqua')
    #m.fillcontinents(color='red',lake_color='blue')
    # draw parallels and meridians.
    #m.drawparallels(np.arange(-90.,91.,30.))
    #m.drawmeridians(np.arange(-180.,181.,60.))
    #m.drawmapboundary(fill_color='aqua')
    return m

#plot point
m = createMap()
l = loadDB()
t = loadTraces()
print(t)
for row in l.values():
    lat, lon = float(row['lat']), float(row['long'])
    m.plot(lon, lat, latlon=True, color='blue', marker='o')
plt.title("Mercator Projection")
plt.show()
