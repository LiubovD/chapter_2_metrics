import glob, os.path, arcpy
from arcpy.sa import *



# Set a new workspace, overriding the passed-down workspace
arcpy.env.workspace = r"D:\Luba\data\Project_americanview\drough\2017_drought"
arcpy.env.scratchWorkspace = r"D:\Luba\data\Project_americanview\drough\2017_drought"
arcpy.env.overwriteOutput = True
os.chdir(r"D:\Luba\data\Project_americanview\drough\2017_drought")
shpfiles = [f for f in glob.glob("*.shp")]
print(shpfiles)
clip_features = r"D:\Luba\data\Project_americanview\drough\towns\towns.shp"

for shpfile in shpfiles:
    feature_cliped = 'RI_' + shpfile
    arcpy.analysis.Clip(shpfile, clip_features, feature_cliped)
    print("Extracting_" + shpfile)
    out_coor_system = arcpy.SpatialReference('NAD 1983 StatePlane Rhode Island FIPS 3800 (Meters)')
    print("Projecting_" + shpfile)
    feature_projected = 'RI_proj' + shpfile
    arcpy.management.Project(feature_cliped, feature_projected, out_coor_system)
    arcpy.conversion.PolygonToRaster(feature_projected, 'DM', "rstr" + shpfile + '.tif', cellsize=20, build_rat='BUILD')
    print("Polygon to raster_" + shpfile)
    # Set the extent environment using a raster
    arcpy.env.extent = r'D:\Luba\data\Project_americanview\drough\towns\towns.shp'
    remap = arcpy.sa.RemapValue([['NODATA', 0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    newRaster = arcpy.sa.Reclassify("rstr" + shpfile + '.tif', "Value", remap)
    newRaster.save(r'D:\Luba\data\Project_americanview\drough\2017_drought\rasters\'' + shpfile + '.tif')
    print("Reclassify_" + shpfile)

os.chdir(r"D:\Luba\data\Project_americanview\drough\2017_drought\rasters")
rasters = [f for f in glob.glob("*.tif")]
counter=0
for file in rasters:
    if counter == 0:
        sum = Raster(file)
        counter += 1
    else:
        sum += Raster(file)
        counter += 1
print(sum)
sum.save(r"D:\Luba\data\Project_americanview\drough\2017_drought\rasters\raster_sum.tif")
Mean = Raster(sum/counter)
Mean.save(r"D:\Luba\data\Project_americanview\drough\2017_drought\rasters\raster_mean.tif")

