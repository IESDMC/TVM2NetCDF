from mpl_toolkits.basemap import Basemap
import netCDF4 as nc # read nc files
import numpy as np # processing data array
import matplotlib.pyplot as plt # plot
import matplotlib.cm as cm        # color map

# show metadata information
rootgrp = nc.Dataset('KIM2005.nc')  
print (rootgrp) 

# extract the lat, lon, and depth information and store as numpy arrays
lat = rootgrp.variables['latitude'][:]
lon = rootgrp.variables['longitude'][:]
dep = rootgrp.variables['depth'][:]
vs = rootgrp.variables['vs'][:]
vp = rootgrp.variables['vp'][:]
vpvs = rootgrp.variables['vpvs'][:]

# convert 1D lat/lon to 2D lat/lon arrays
lon2,lat2=np.meshgrid(lon,lat) 

# extract vp at first depth step (0), all lat/lon (:)
depthIndex = 15
vs_0 = rootgrp.variables['vs'][depthIndex,:,:]
print(vs_0)
# map, basic projection and layout 
begla = 21.3
beglo = 119.0
endla = 25.8
endlo = 123.0
fig = plt.figure(figsize=(12,10))
m = Basemap(projection='cyl',llcrnrlat=begla, urcrnrlat=endla,\
            llcrnrlon=beglo, urcrnrlon=endlo, resolution='h')
m.drawcoastlines()   # coastline
parallels = np.arange(-90.,90,1.)
meridians = np.arange(0.,360.,1.)
vpCptLevel = [1,2,3,4,5,6,7,8,9]
vsCptLevel = [0.2,1.6,2.2,2.8,3.4,4.2,5.0]
vsvpCptLevel = [1.40,1.65,1.73,1.80,2.10]
m.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)  # latitude label
m.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)  # longitude label

cx,cy =m(lon2,lat2)  # convert to map projection coordinate
CS = m.pcolormesh(cx,cy,vs_0,cmap=cm.jet,shading='gouraud')
plt.colorbar(CS,orientation='horizontal',label='Vs (km/s)', ticks=vsCptLevel,fraction=0.04, pad=0.04)
plt.title('KIM2005.nc'+'     depth:'+str(1+depthIndex*2)+'km')
plt.show()

