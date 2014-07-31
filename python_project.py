###Convert GPX to feature
import sys
import arcpy
from arcpy import env

arcpy.AddMessage(sys.argv)
if sys.argv[1].split('.')[1] == 'gpx':
    env.overwriteoutput = True
    arcpy.GPXtoFeatures_conversion(sys.argv[1], sys.argv[2])
###Convert KML to Layer
elif sys.argv[1].split('.')[1] == 'kml':
    env.overwriteoutput = True
    arcpy.KMLToLayer_conversion(sys.argv[1], sys.argv[2])
