import arcpy
import os

# Batch Slope Calculation
# Calculates slope from multiple raster inputs
# Requires ArcGIS Spatial Analyst extension

input_folder = r"C:\GIS\rasters"
output_folder = r"C:\GIS\output\slope"

arcpy.env.workspace = input_folder
arcpy.env.overwriteOutput = True

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

arcpy.CheckOutExtension("Spatial")

rasters = arcpy.ListRasters()

if not rasters:
    print("No rasters found in input folder.")
else:
    for raster in rasters:
        try:
            print(f"Processing: {raster}")
            slope_output = arcpy.sa.Slope(raster, "DEGREE")
            out_path = os.path.join(output_folder, f"slope_{raster}")
            slope_output.save(out_path)
            print(f"  Saved: {out_path}")
        except Exception as e:
            print(f"  Failed on {raster}: {e}")

arcpy.CheckInExtension("Spatial")
print("Batch slope processing complete.")
