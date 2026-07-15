"""
UrbanChangeAI: Configuration management system.
Defines satellite bands, machine learning hyperparameters, and the names of all 50+ geospatial indices.
"""

from typing import Dict, Any, Optional, List

class Config:
    """
    Centralized configuration engine holding factory defaults 
    and allowing dictionary-based programmatic overrides.
    """
    
    def __init__(self, overrides: Optional[Dict[str, Any]] = None):
        # 1. إعدادات محرك الحساب السحابي (Google Earth Engine Settings)
        self._defaults: Dict[str, Any] = {
            "gee_project_id": None,  # يترك فارغاً ليعتمد على المشروع الافتراضي للمستخدم
            "cloud_cover_threshold": 15.0,  # الحد الأقصى المسموح به لنسبة الغيوم في الصور
            "spatial_resolution": 10,  # دقة العينات الحيزية بالأمتار (Sentinel-2 الافتراضية)
        }
        
        # 2. إعدادات بيانات الأقمار الصناعية وحزم الطيف (Satellite Bands Mapping)
        self._defaults["satellite_platforms"] = ["Sentinel-2", "Landsat-8", "Landsat-9"]
        self._defaults["bands_sentinel2"] = {
            "BLUE": "B2", "GREEN": "B3", "RED": "B4", "RE1": "B5", 
            "RE2": "B6", "RE3": "B7", "NIR": "B8", "RE4": "B8A", 
            "SWIR1": "B11", "SWIR2": "B12"
        }
        
        # 3. حصر وتحديد الـ 50 مؤشرًا جيو-مكانيًا المطلوب حسابها
        # مقسمة هندسياً إلى مؤشرات طيفية (تُحسب سحابياً) ومؤشرات حيزية ولاندسكيب (تُحسب محلياً)
        self._defaults["spectral_indices"] = [
            # مؤشرات الغطاء النباتي (Vegetation Indices)
            "NDVI", "SAVI", "EVI", "ARVI", "GARI", "GNDVI", "IPVI", "OSAVI", "MSAVI2", "RDVI",
            # مؤشرات المناطق الحضرية والمبنية (Built-up & Urban Indices)
            "NDBI", "IBI", "BSI", "EBBI", "UI", "NDBLI", "MNDBI", "BRBA", "BAEI", "NBI",
            # مؤشرات المياه والرطوبة (Water & Moisture Indices)
            "NDWI", "MNDWI", "NDTI", "NDSI", "AWEI", "WI", "WRI", "LSWI", "NDII", "SRWI",
            # مؤشرات التربة والأسطح المتقدمة (Soil & Advanced Surface Indices)
            "DBI", "ENDISI", "MNDISI", "LST", "UEI", "LEI"
        ]
        
        self._defaults["landscape_metrics"] = [
            # مؤشرات السيماء الحيزية ولاندسكيب الحضرية عبر PyLandStats
            "shannon_entropy", "compactness", "patch_density", "edge_density",
            "fractal_dimension", "aggregation_index", "number_of_patches",
            "total_edge", "landscape_shape_index", "largest_patch_index",
            "mean_patch_area", "contagion_index", "cohesion_index", "shannon_diversity"
        ]
        
        # 4. معلمات خوارزميات التعلم الآلي والعميق (Machine & Deep Learning Hyperparameters)
        self._defaults["ml_algorithm"] = "xgboost"  # الخيار الافتراضي: 'random_forest', 'xgboost', 'pytorch'
        
        self._defaults["xgboost_params"] = {
            "n_estimators": 200,
            "max_depth": 6,
            "learning_rate": 0.1,
            "subsample": 0.8,
            "colsample_bytree": 0.8,
            "random_state": 42,
            "eval_metric": "mlogloss"
        }
        
        self._defaults["random_forest_params"] = {
            "n_estimators": 150,
            "max_depth": 12,
            "min_samples_split": 5,
            "random_state": 42,
            "n_jobs": -1
        }
        
        self._defaults["pytorch_params"] = {
            "model_architecture": "UNet",  # الهيكل البرمجي للتصنيف الدلالي
            "batch_size": 32,
            "epochs": 50,
            "learning_rate": 0.001,
            "weight_decay": 1e-4,
            "hidden_units": [64, 32]
        }
        
        # 5. تصنيفات غطاء الأرض المستهدفة (Land Cover Classes)
        self._defaults["target_classes"] = {
            1: "Built-up/Urban",    # المناطق الحضرية والمباني
            2: "Vegetation/Cropland", # الغطاء النباتي والمزارع
            3: "Water Bodies",      # المسطحات المائية
            4: "Bare Soil/Desert"   # التربة العارية والأراضي المفتوحة
        }
        
        # 6. إعدادات التصدير واللوحات الرسومية (Export & Theme Styling)
        self._defaults["theme_color"] = "#1E3A8A"  # الأزرق الداكن للتقارير والخرائط
        self._defaults["visualization_palette"] = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"]
        
        # دمج أي تعديلات ممررة من المستخدم وتخطي الإعدادات الافتراضية
        if overrides:
            self._update_config(overrides)

    def _update_config(self, overrides: Dict[str, Any]) -> None:
        """Recursive update helper for dictionary configuration tree overrides."""
        for key, value in overrides.items():
            if isinstance(value, dict) and key in self._defaults and isinstance(self._defaults[key], dict):
                self._defaults[key].update(value)
            else:
                self._defaults[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieves a specific configuration parameter value.
        """
        return self._defaults.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """Sets or live changes a configuration property value."""
        self._defaults[key] = value

    @property
    def all_indices_count(self) -> int:
        """Calculates total integrated target metrics to ensure 50+ index metrics."""
        return len(self._defaults["spectral_indices"]) + len(self._defaults["landscape_metrics"])
