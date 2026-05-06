# GIS & Remote Sensing Portfolio – Donald Andrade

## Overview
This portfolio demonstrates my experience in GIS, remote sensing, and spatial data processing, with a focus on environmental analysis and workflow automation using Python (ArcPy).

I am particularly interested in applying geospatial data to real-world environmental and agricultural problems.

---

## 🗺️ Key Project: Land Suitability Mapping (Micro-Watershed)

### Description
Developed a land suitability model using multiple environmental parameters to support watershed-level decision-making.

### Methodology
- Integrated soil, slope, texture, and terrain datasets
- Classified land into suitability classes:
  - S1: Highly Suitable
  - S2: Moderately Suitable
  - S3: Marginally Suitable
- Produced multiple thematic GIS maps

### Tools
ArcGIS Pro

---

## 📍 Sample Maps

### Slope Map
![Slope Map](maps/slope.jpg)

### Soil Map
![Soil Map](maps/soil.jpg)

### Erosion Map
![Erosion Map](maps/erosion.jpg)

### Texture Map
![Texture Map](maps/texture.jpg)

---

## 📊 Map Catalogue

A compiled GIS atlas containing all thematic maps used in this watershed analysis project.

📄 [View Map Catalogue](docs/map_catalog.pdf)

---

## 🧠 GIS Automation (Python – ArcPy)

The following script automates batch raster processing using ArcPy.

import arcpy
import os

# ----------------------------
# INPUT DATA
# ----------------------------
satellite_raster = r"C:\GIS\input\satellite.tif"
soil_polygons = r"C:\GIS\input\soil_zones.shp"
field_points = r"C:\GIS\input\field_samples.shp"

output_gdb = r"C:\GIS\output\project.gdb"

arcpy.env.workspace = output_gdb
arcpy.env.overwriteOutput = True

# ----------------------------
# STEP 1: ZONE GENERATION FROM SATELLITE IMAGE
# (example: unsupervised classification or raster reclassification)
# ----------------------------

classified_raster = os.path.join(output_gdb, "soil_zones_raster")

# Example placeholder: reclassify or segmentation output
# (Assumes raster is already prepared or classified in ArcGIS tools)
arcpy.sa.Reclassify(
    satellite_raster,
    "Value",
    arcpy.sa.RemapRange([[0, 50, 1], [50, 100, 2], [100, 150, 3]])
).save(classified_raster)

print("Satellite zones created")

# ----------------------------
# STEP 2: CONVERT RASTER ZONES TO POLYGONS
# ----------------------------

zone_polygons = os.path.join(output_gdb, "soil_zones_poly")

arcpy.conversion.RasterToPolygon(
    classified_raster,
    zone_polygons,
    "NO_SIMPLIFY",
    "Value"
)

print("Raster converted to polygons")

# ----------------------------
# STEP 3: JOIN FIELD DATA TO ZONES
# ----------------------------

zone_with_fields = os.path.join(output_gdb, "zones_with_field_data")

arcpy.analysis.SpatialJoin(
    zone_polygons,
    field_points,
    zone_with_fields,
    join_type="KEEP_ALL",
    match_option="INTERSECT"
)

print("Field data joined to zones")

# ----------------------------
# STEP 4: ZONE STATISTICS (VALIDATION STEP)
# ----------------------------

stats_table = os.path.join(output_gdb, "zone_statistics")

arcpy.sa.ZonalStatisticsAsTable(
    zone_polygons,
    "gridcode",
    satellite_raster,
    stats_table,
    "DATA",
    "MEAN"
)

print("Zone statistics calculated")
### Workflows
- Batch raster processing
- Automated spatial analysis
- Data cleaning and validation

📂 Script available in `/scripts`

---

## 🎓 Master’s Thesis (Ongoing)

**Field Phenotyping of Buckwheat using UAV, Fluorescence, and LAI Modelling**

- Integration of UAV imagery with field measurements
- Multi-temporal dataset analysis
- Comparison of modeled vs observed LAI

---

## 🛠️ Tools & Technologies
- GIS: ArcGIS Pro, QGIS, SNAP, ERDAS Imagine  
- Programming: Python (ArcPy)  
- Spatial Analysis: Raster processing, classification, mapping  
- Data Handling: SQL basics, R

---

## 📬 Contact
Email: donaldandrade04@gmail.com  
Location: Poznań, Poland
