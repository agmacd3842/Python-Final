###Convert GPX to feature
import arcpy
from arcpy import env
env.overwriteoutput = True
arcpy.GPXtoFeatures_conversion()
arcpy.SelectLayerByAttribute_management()
arcpy.PointsToLine_management()
###Convert KML to Layer
outLocation = ["CURRENT"]
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
