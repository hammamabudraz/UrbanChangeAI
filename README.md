# 🏙️ UrbanChangeAI

An enterprise-grade, high-level **AI & GIS Python library** designed for automated multi-temporal satellite imagery classification, ecosystem indicator modeling, and urban change detection using **Google Earth Engine (GEE)**, **PyTorch**, and **XGBoost**.

With **UrbanChangeAI**, what used to take months of manual GIS modeling and remote sensing computation is reduced to **a single line of Python code**.

---

## ✨ Key Architectural Features

*   **Zero-Infrastructure Cloud Computing:** Leveraging Google Earth Engine (GEE) servers for cloud filtering and massive grid processing.
*   **High-Density Metric Engine (50+ Indices):** Fully computes 30+ multi-spectral & thermal indices (NDVI, SAVI, EVI, NDBI, IBI, LST, UEI, etc.) stacked on the cloud, paired with 14+ landscape architecture metrics (Shannon Entropy, Compactness, Patch Density) calculated locally.
*   **Hybrid AI Predictive Pipelines:** Runs local optimized **PyTorch Deep UrbanNet**, **XGBoost**, or **Scikit-Learn** model layers.
*   **Multi-Format Enterprise Reporting:** Instantly compiles vector outputs and data arrays into customized **Excel Workbooks**, **GIS GeoJSON Layers**, **PDF Executive Summaries**, and editable **MS Word Documents**.
*   **No-Code Interface:** Built-in web interactive control panel powered by **Streamlit** and **Folium** maps.

---

## ⚙️ Installation

```bash
pip install urbanchangeai
```

---

## 🚀 Quickstart Usage (The Facade Pattern)

```python
from urbanchangeai import UrbanChange

# Initialize project targeting spatial boundaries and chronological intervals
project = UrbanChange(
    country="Palestine",
    region="Gaza Strip",
    years=[2023, 2026],
    config_override={"ml_algorithm": "xgboost"}
)

# Execute full pipeline: download -> process -> compute -> AI classify -> export
project.run()
```

---

## 🎛️ Launching the Interactive UI Dashboard

```python
from urbanchangeai import UrbanChange

project = UrbanChange(country="Palestine", region="Gaza Strip", years=[2023, 2026])
project.launch_dashboard()
```
