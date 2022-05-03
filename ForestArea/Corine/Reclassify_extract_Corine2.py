# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
from arcpy import os
# Set environment settings
#env.workspace = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC"
# Set Snap Raster environment
workdir = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CLC"

inRaster = workdir + "/U2000_CLC1990_V2020_20u1.tif"
inRaster2 = workdir + "/U2006_CLC2000_V2020_20u1.tif"
inRaster3 = workdir + "/U2018_CLC2012_V2020_20u1.tif"
inRaster4 = workdir + "/U2018_CLC2018_V2020_20u1.tif"
inRaster5 = workdir + "/U2012_CLC2006_V2020_20u1.tif"

reclassField = "Value"
remapBLF = RemapValue([["23", "1"]])
remapCF = RemapValue([["24", "1"]])
remapMF = RemapValue([["25", "1"]])
remapTWS = RemapValue([["29", "1"]])
# #1=BLF, 2=CF, 3=MF



rasters = [inRaster, inRaster2, inRaster3, inRaster4, inRaster5]

remaps = {remapBLF:"remapBLF", \
          remapCF:"remapCF", remapMF:"remapMF", \
          remapTWS:"remapTWS"}

for e, ras in enumerate(rasters):
    if e == 0:
        for remap, remap_name in remaps.iteritems():
            ras_name = workdir + "/output/" + ras[-19:-15] + "_" + remap_name + ".tif"
            reclassified = Reclassify(ras, reclassField, remap, "NODATA")
            reclassified.save(ras_name)
            #table_name = ras[:-4] + "_" + remap_name + ".dbf"
            table_name = workdir + "/output/" + ras[-19:-15] + "_" + remap_name + ".dbf"
            ZonalStatisticsAsTable("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC/Countries_extended100m.tif", "Value", ras_name, table_name, "DATA", "SUM")
            print(ras_name)
            print(table_name)