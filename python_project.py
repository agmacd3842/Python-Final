###Convert GPX to feature
import sys
import arcpy
from arcpy import env

arcpy.AddMessage(sys.argv)
if sys.argv[1].split('.')[1] == 'gpx':
    env.overwriteoutput = True
    arcpy.GPXtoFeatures_conversion(sys.argv[1], sys.argv[2])
##    arcpy.SelectLayerByAttribute_management('in_memory\newfile', 'NEW_SELECTION', "\"Type\" = 'TRKPT'")
    arcpy.PointsToLine_management('newfile', sys.argv[2], 'Name', '#', 'NO_CLOSE')
###Convert KML to Layer
elif sys.argv[1].split('.')[1] == 'kml':
    outLocation == ["CURRENT"]
    MasterGDB = ["CURRENT"]
    MasterGDBLocation = ["CURRENT"]
    arcpy.CreateFileGDB_management(outLocation, MasterGDB)
    for kmz in arcpy.ListFiles('*.KM*'):
        print "CONVERTING: " + OS.path.join(arcpy.env.workspace,kmz)
        arcpy.KMLToLayer_conversion(kmz, outLocation)
    arcpy.env.workspace = outLocation
    wks = arcpy.ListWorkspaces('*' , 'FileGDB')
    wks.remove(MasterGDBLocation)
    for fgdb in wks:
        arcpy.env.workspace = fgdb
        featureClasses = arcpy.ListFeatureClasses('*', '', 'Placemarks')
        for fc in featureClasses:
            print "COPYING: " + fc + "FROM: " + fgdb
            fcCopy = fgdb + os.sep + 'Placemarks' + os.sep + fc
            arcpy.FeatureClassToFeatureClass_conversion(fcCopy, MasterGDBLocation, fgdb[fgdb.rfind(os.sep) + 1: -4])
            del kmz, wks, fc, featureClasses, fgdb
