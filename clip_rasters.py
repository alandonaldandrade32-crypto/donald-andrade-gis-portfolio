import arcpy
import os

# Batch Raster Clip to Study Area Boundary
# Clips all rasters in input folder to a polygon boundary
# Requires ArcGIS Pro

input_folder  = r"C:\GIS\rasters"
output_folder = r"C:\GIS\output\clipped"
clip_boundary = r"C:\GIS\boundaries\study_area.shp"

arcpy.env.workspace = input_folder
arcpy.env.overwriteOutput = True

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

rasters = arcpy.ListRasters()

if not rasters:
    print("No rasters found.")
else:
    for raster in rasters:
        try:
            print(f"Clipping: {raster}")
            out_path = os.path.join(output_folder, f"clipped_{raster}")
            arcpy.management.Clip(
                in_raster=raster,
                rectangle="",
                out_raster=out_path,
                in_template_dataset=clip_boundary,
                clipping_geometry="ClippingGeometry",
                maintain_clipping_extent="NO_MAINTAIN_EXTENT"
            )
            print(f"  Saved: {out_path}")
        except Exception as e:
            print(f"  Failed on {raster}: {e}")

print("Batch clipping complete.")
