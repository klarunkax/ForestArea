import arcpy
arcpy.MakeNetCDFRasterLayer_md("C:/Users/Klara/Documents/Prace/JRC/Teleworking/2022/Forest area EU/Data/ESA_LC/C3S-LC-L4-LCCS-Map-300m-P1Y-2018-v2.1.1.nc","lccs_class",
                         "lon","lat","2018")
