# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *
from arcpy import os

# Set environment settings
env.workspace = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT"

inRaster = "FTY_2012_100m_eu_03035_d02_full.tif"
inRaster2 = "FTY_2015_100m_eu_03035_d02_full.tif"
inRaster3 = "FTY_2018_100m_eu_03035_V1_0.tif"

#1=BLF, 2=CF, 3=MF
reclassField = "Value"
remapF = RemapValue([["1", "1"], ["2", "1"], ["3", "1"]])
remapBLF = RemapValue([["1", "1"]])
remapCF = RemapValue([["2", "1"]])
remapMF = RemapValue([["3", "1"]])


CLCreclass2012F = Reclassify(inRaster, reclassField, remapF, "NODATA")
CLCreclass2012BLF = Reclassify(inRaster, reclassField, remapBLF, "NODATA")
CLCreclass2012CF = Reclassify(inRaster, reclassField, remapCF, "NODATA")
CLCreclass2012MF = Reclassify(inRaster, reclassField, remapMF, "NODATA")

CLCreclass2015F = Reclassify(inRaster2, reclassField, remapF, "NODATA")
CLCreclass2015BLF = Reclassify(inRaster2, reclassField, remapBLF, "NODATA")
CLCreclass2015CF = Reclassify(inRaster2, reclassField, remapCF, "NODATA")
CLCreclass2015MF = Reclassify(inRaster2, reclassField, remapMF, "NODATA")

CLCreclass2018F = Reclassify(inRaster3, reclassField, remapF, "NODATA")
CLCreclass2018BLF = Reclassify(inRaster3, reclassField, remapBLF, "NODATA")
CLCreclass2018CF = Reclassify(inRaster3, reclassField, remapCF, "NODATA")
CLCreclass2018MF = Reclassify(inRaster3, reclassField, remapMF, "NODATA")

CLCreclass2012F.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2012F.tif")
CLCreclass2012BLF.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2012BLF.tif")
CLCreclass2012CF.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2012CF.tif")
CLCreclass2012MF.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2012MF.tif")

CLCreclass2015F.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2015F.tif")
CLCreclass2015BLF.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2015BLF.tif")
CLCreclass2015CF.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2015CF.tif")
CLCreclass2015MF.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2015MF.tif")

CLCreclass2018F.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2018F.tif")
CLCreclass2018BLF.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2018BLF.tif")
CLCreclass2018CF.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2018CF.tif")
CLCreclass2018MF.save("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify/CLCreclass2018MF.tif")
