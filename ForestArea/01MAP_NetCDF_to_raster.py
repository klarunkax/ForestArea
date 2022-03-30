import os
import arcpy
from arcpy import env
from arcpy.sa import *

work_dir = r"C:\Users\Klara\Documents\Prace\JRC\Teleworking\2022\Forest area EU\Data\ESA_LC"

# local variables - netcdf
variable = "lccs_class"
x_dimension = "lon"
y_dimension = "lat"
band_dimension = ""
dimension = "time"
dimension_values = ""
valueSelectionMethod = ""

arcpy.env.workspace = work_dir

for nc_file in arcpy.ListFiles("*.nc"):
    tiff_file = os.path.splitext(nc_file)[0] + ".tif"
    print "- - - - - -"
    print nc_file + " - " + tiff_file
    outRasterLayer = "raster_layer"

    arcpy.MakeNetCDFRasterLayer_md(work_dir + "//" + nc_file, variable, x_dimension, y_dimension, \
                                   outRasterLayer, band_dimension, dimension_values, \
                                   valueSelectionMethod)
    arcpy.CopyRaster_management(outRasterLayer, work_dir + "//" + tiff_file, "", "", "", \
                                "NONE", "NONE", "")
    arcpy.Delete_management(outRasterLayer, "")
    del outRasterLayer
    
    ## delete files
    ovr_file = os.path.splitext(nc_file)[0] + ".tif.ovr"
    arcpy.Delete_management(work_dir + "//" + ovr_file)
    xml1_file = os.path.splitext(nc_file)[0] + ".tif.aux.xml"
    arcpy.Delete_management(work_dir + "//" + xml1_file)
    xml2_file = os.path.splitext(nc_file)[0] + ".tif.xml"
    arcpy.Delete_management(work_dir + "//" + xml2_file)

print "done"
