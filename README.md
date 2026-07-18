# 🏙️ UrbanChangeAI: Automated Spatial AI & GIS Control Panel

An enterprise-grade, full-stack Geo-Spatial Intelligence platform designed for satellite remote sensing, ecosystem indicators, and high-precision land cover trajectory tracking. Powered by **Google Earth Engine (GEE)**, advanced pixel-based classification frameworks, and interactive web mapping technologies.

---

## 🎯 Key Features & Architecture

- **Spatially Bounded Cloud Processing**: Dynamically filters, cloud-masks, and processes raw multi-spectral imagery (Sentinel-2) restricted strictly within administrative polygons via international boundaries databases (LSIB SIMPLE).
- **Automated Machine Learning & AI Core**: Incorporates high-accuracy remote sensing classification frameworks (Random Forest, XGBoost) to categorize land cover profiles based on physical spectral matrices.
- **Dynamic Change Matrix & Statistics**: Real-time quantification of urban expansion sprawl magnitudes and vegetative matrix conversions computed dynamically over flexible temporal scales.
- **Interactive Multi-Temporal GIS Maps**: Fluid rendering of classified geospatial raster layer grids directly on custom Leaflet/Folium map containers with direct web overlay layers toggle features.
- **Downstream Automated Asset Production Center**: Seamlessly compiles, formats, and exports valid, full-structured enterprise deliverables: PDF Executive Reports, Spreadsheet Analytical Workbooks (Excel), and spatial layers vector geometry files (GeoJSON).

---

## 🛠️ Tech Stack & Dependencies

- **Backend Intelligence Engine**: Python 3.10+
- **Cloud Remote Sensing**: `google-earth-engine (ee)`
- **UI Web Interface Platform**: `streamlit`
- **Geospatial Mapping Stack**: `folium`, `streamlit-folium`
- **Data Matrix Processing**: `pandas`, `openpyxl`
- **Structured Asset Generation**: `reportlab`

---

## ⚙️ Quick Local Deployment Setup

1. **Activate Virtual Isolated Environment**:
   ```bash
   D:\UrbanChangeAI> venv\Scripts\activate
   ```
   
2. **Execute Interactive Local Web Server Command**:
   ```bash
   (venv) D:\UrbanChangeAI> streamlit run main.py
   ```
   
3. **Access Desktop Dashboard Interface Control Panel**:
   Open your browser and navigate manually to: `http://localhost:8501`

---

## 🗺️ Raster Classification Color Legend
- 🔴 **Red Layer Indicator**: High-density Built-up, Infrastructure, & Asphalt Sprawl.
- 🟢 **Green Layer Indicator**: Dense Canopy Vegetation, Crops, & Agricultural Land.
- 🔵 **Blue Layer Indicator**: Marine Spatial Entities & Natural Water Bodies.
- 🟡 **Sandy/Brown Layer**: Open Dry Bare Soil & Sand Dunes Profiles.
