import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/CopernicusFT/output_reclassify"
##
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2012F.tif",
                                 "statCOP2012F.dbf", "DATA", "SUM")
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2012BLF.tif",
                                 "statCOP2012BLF.dbf", "DATA", "SUM")
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2012CF.tif",
                                 "statCOP2012CF.dbf", "DATA", "SUM")
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2012MF.tif",
                                 "statCOP2012MF.dbf", "DATA", "SUM")
##
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2015F.tif",
                                 "statCOP2015F.dbf", "DATA", "SUM")
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2015BLF.tif",
                                 "statCOP2015BLF.dbf", "DATA", "SUM")
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2015CF.tif",
                                 "statCOP2015CF.dbf", "DATA", "SUM")
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2015MF.tif",
                                 "statCOP2015MF.dbf", "DATA", "SUM")
##
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2018F.tif",
                                 "statCOP2018F.dbf", "DATA", "SUM")
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2018BLF.tif",
                                 "statCOP2018BLF.dbf", "DATA", "SUM")
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2018CF.tif",
                                 "statCOP2018CF.dbf", "DATA", "SUM")
ZonalStatisticsAsTable("Countries_extended100m.tif", "Value", "CLCreclass2018MF.tif",
                                 "statCOP2018MF.dbf", "DATA", "SUM")
