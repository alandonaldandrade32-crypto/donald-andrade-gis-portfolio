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

```python
import arcpy
import os

# Input folder containing raster files
input_folder = r"C:\GIS\rasters"
output_folder = r"C:\GIS\output"

arcpy.env.workspace = input_folder
arcpy.env.overwriteOutput = True

rasters = arcpy.ListRasters()

for raster in rasters:
    try:
        print(f"Processing: {raster}")

        # Slope calculation (Spatial Analyst required)
        slope = arcpy.sa.Slope(raster)

        output_path = os.path.join(output_folder, f"slope_{raster}")

        slope.save(output_path)

        print(f"Saved: {output_path}")

    except Exception as e:
        print(f"Failed on {raster}: {e}")

print("Processing complete.")
```

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
