import arcpy

# NDVI Calculation from Multispectral Raster
# Input: separate Red and NIR band rasters
# Output: NDVI raster
# Requires ArcGIS Spatial Analyst extension

red_band_path = r"C:\GIS\rasters\red_band.tif"
nir_band_path = r"C:\GIS\rasters\nir_band.tif"
output_path   = r"C:\GIS\output\ndvi\ndvi_output.tif"

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")

try:
    red = arcpy.sa.Float(arcpy.Raster(red_band_path))
    nir = arcpy.sa.Float(arcpy.Raster(nir_band_path))

    ndvi = (nir - red) / (nir + red)
    ndvi.save(output_path)
    print(f"NDVI saved to: {output_path}")

except Exception as e:
    print(f"Error: {e}")

finally:
    arcpy.CheckInExtension("Spatial")
