
#Import gdal
from osgeo import gdal
from pathlib import Path
from os import walk
import os.path

import matplotlib.colors
import numpy as np


import struct
filepath = "C:/Users/anne1/GRACE/GRACE/"
filenames = next(walk(filepath), (None, None, []))[2]  # [] if no file
out_path = "./output/"
variable = 'lwe_thickness' #"WVEL"

other_proj = gdal.Open("C:/Users/anne1/GRACE/ECCO/nc/OCEAN_VELOCITY_mon_mean_2014-11_ECCO_V4r4_latlon_0p50deg.ncband_3.tif")


#Open existing dataset
suffix = ".nc"
#for i in range(0,len(filenames)):
for i in range(0,len(filenames)):
    if(filenames[i].endswith(suffix)):

        
        src_ds =gdal.Open('NETCDF:"'  + filepath + filenames[i] + '":' + variable)
        
        #print(src_ds)
        #Open output format driver, see gdal_translate --formats for list
        format = "GTiff"        
        driver = gdal.GetDriverByName( format )

        #Output to new format
        #dst_ds = driver.CreateCopy(filenames[i], src_ds, 0)
        
        #if np.max(lon) > 180


        ulx, xres, xskew, uly, yskew, yres  = src_ds.GetGeoTransform() #max/min value of longitude and latitude
        lon = ulx + (src_ds.RasterXSize * xres) #lon
        lat = uly + (src_ds.RasterYSize * yres) 

        print('uly', uly, 'yres', yres, 'lat' , lat )
        print('ulx', ulx, 'xrex', xres, 'lon' , lon )

        #print(1, src_ds.RasterCount +1)
        for j in range(1, src_ds.RasterCount +1 ): #Save bands as individual files         
         
                if not os.path.exists(out_path + filenames[i] + '_band_' + str(j) + '.tif'):
                   
                    out_ds = gdal.Translate(out_path + filenames[i] + '_band_' + str(j) + '.tif', src_ds, format='GTiff', bandList=[j])
             
                    out_ds = None
     
        src_ds = None



