# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
from arcpy import os
# Set environment settings
#env.workspace = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC"
# Set Snap Raster environment
workdir = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/modis"
inRaster = workdir + "/2001.tif"
inRaster2 = workdir + "/2005.tif"
inRaster3 = workdir + "/2006.tif"
inRaster4 = workdir + "/2010.tif"
inRaster5 = workdir + "/2012.tif"
inRaster6 = workdir + "/2015.tif"
inRaster7 = workdir + "/2018.tif"
inRaster8 = workdir + "/2020.tif"
#

reclassField = "Value"
remap11 = RemapValue([["11", "1"]])
remap12 = RemapValue([["12", "1"]])
remap13 = RemapValue([["13", "1"]])
remap14 = RemapValue([["14", "1"]])
remap15 = RemapValue([["15", "1"]])
remap16 = RemapValue([["16", "1"]])
remap21 = RemapValue([["21", "1"]])
remap22 = RemapValue([["22", "1"]])



rasters = [inRaster, inRaster2, inRaster3, inRaster4, inRaster5, inRaster6, inRaster7, inRaster8]
remaps = {remap11:"remap11", remap12:"remap12"
          , remap13:"remap13", remap14:"remap14", \
          remap15:"remap15", remap16:"remap16", \
           remap21:"remap21",remap22:"remap22", \
}

for e, ras in enumerate(rasters):
    if e == 7:
        for remap, remap_name in remaps.iteritems():
            ras_name = ras[:-4] + "_" + remap_name + ".tif"
            reclassified = Reclassify(ras, reclassField, remap, "NODATA")
            reclassified.save(ras_name)
            table_name = workdir + "/output/" + ras[-8:-4] + "_" + remap_name[5:] + ".dbf"
            ZonalStatisticsAsTable("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC/Countries_extended100m.tif", "Value", ras_name, table_name, "DATA", "SUM")
            print(table_name)
            print(ras_name)