# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
from arcpy import os
# Set environment settings
#env.workspace = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC"
# Set Snap Raster environment
workdir = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT"
inRaster = workdir + "/FTY_2012_100m_eu_03035_d02_full.tif"
inRaster2 = workdir + "/FTY_2015_100m_eu_03035_d02_full.tif"
inRaster3 = workdir + "/FTY_2018_100m_eu_03035_V1_0.tif"

#
reclassField = "Value"
remapF = RemapValue([["1", "1"], ["2", "1"], ["3", "1"]])
remapBLF = RemapValue([["1", "1"]])
remapCF = RemapValue([["2", "1"]])
remapMF = RemapValue([["3", "1"]])

# #1=BLF, 2=CF, 3=MF


rasters = [inRaster, inRaster2, inRaster3]
remaps = {remapF:"remapF", remapBLF:"remapBLF", \
          remapCF:"remapCF", remapMF:"remapMF"}

for e, ras in enumerate(rasters):
    if e >= 0:
        for remap, remap_name in remaps.iteritems():
            ras_name = workdir + "/output/" + ras[-31:-28] + "_" + remap_name + ".tif" \
                                                                                "" \
                                                                                "" \
                                                                                ""
            reclassified = Reclassify(ras, reclassField, remap, "NODATA")
            reclassified.save(ras_name)
            #table_name = ras[:-4] + "_" + remap_name + ".dbf"
            table_name = workdir + "/output/" + ras[-31:-28] + "_" + remap_name + ".dbf"
            ZonalStatisticsAsTable("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC/Countries_extended100m.tif", "Value", ras_name, table_name, "DATA", "SUM")
            print(ras_name)
            print(table_name)