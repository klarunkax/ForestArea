# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
from arcpy import os
# Set environment settings
#env.workspace = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC"
# Set Snap Raster environment
workdir = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC"
inRaster = workdir + "/1992.tif"
inRaster2 = workdir + "/1995.tif"
inRaster3 = workdir + "/2000.tif"
inRaster4 = workdir + "/2005.tif"
inRaster5 = workdir + "/2006.tif"
inRaster6 = workdir + "/2010.tif"
inRaster7 = workdir + "/2012.tif"
inRaster8 = workdir + "/2015.tif"
inRaster9 = workdir + "/2018.tif"
inRaster10 = workdir + "/2020.tif"
#
# #1=BLF, 2=CF, 3=MF
reclassField = "Value"
remap30 = RemapValue([["30", "1"]])
remap40 = RemapValue([["40", "1"]])
remap50 = RemapValue([["50", "1"]])
remap60 = RemapValue([["60", "1"], ["61", "1"], ["62", "1"]])
remap70 = RemapValue([["70", "1"], ["71", "1"], ["72", "1"]])
remap80 = RemapValue([["80", "1"], ["81", "1"], ["82", "1"]])
remap90 = RemapValue([["90", "1"]])
remap100 = RemapValue([["100", "1"]])
remap110 = RemapValue([["110", "1"]])
remap160 = RemapValue([["160", "1"]])
remap170 = RemapValue([["170", "1"]])


rasters = [inRaster, inRaster2, inRaster3, inRaster4, inRaster5, inRaster6, inRaster7, inRaster8, inRaster9, inRaster10]
remaps = {remap30:"remap30", remap40:"remap40"}
    # , remap50:"remap50", remap60:"remap60", \
    #       remap70:"remap70", remap80:"remap80", \
    #       remap90:"remap90",remap100:"remap100", \
    #       remap110:"remap110",remap160:"remap160", \
    #       remap170:"remap170"}

for e, ras in enumerate(rasters):
    if e <= 5:
        for remap, remap_name in remaps.iteritems():
            ras_name = ras[:-4] + "_" + remap_name + ".tif"
            reclassified = Reclassify(ras, reclassField, remap, "NODATA")
            reclassified.save(ras_name)
            table_name = workdir + "/output/" + ras[-8:-4] + "_" + remap_name[5:] + ".dbf"
            ZonalStatisticsAsTable("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC/Countries_extended100m.tif", "Value", ras_name, table_name, "DATA", "SUM")
            print(table_name)
            print(ras_name)