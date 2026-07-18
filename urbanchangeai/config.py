"""
UrbanChangeAI - Configuration Module
"""

class UrbanConfig:
    def __init__(self):
        # المعرف السحابي لشركاء جوجل
        self.gee_project_id = "round-gamma-465907-v7"
        
        # خوارزمية الذكاء الاصطناعي الافتراضية للتدريب والتصنيف
        self.ml_algorithm = "xgboost"
        
        # دقة الأقمار الصناعية المستهدفة (أمتار) وحزمة الفلترة الطيفية
        self.spatial_resolution = 10
        self.cloud_cover_threshold = 10
        
        # تصنيفات الأغطية الأرضية الأربعة الأساسية (IPCC Standard)
        self.land_cover_classes = {
            1: "Urban/Built-up",
            2: "Vegetation",
            3: "Water Bodies",
            4: "Bare Soil"
        }
        
        # إعدادات معالجة النسيج الحيزي واللاندسكيب
        self.landscape_metrics = [
            "shannon_entropy", 
            "compactness", 
            "patch_density", 
            "edge_density", 
            "fractal_dimension", 
            "aggregation_index"
        ]

# حيلة هندسية ذكية: جعل الاسم القديم يشير إلى الكلاس الجديد لمنع تعطل الموديولات الداخلية
Config = UrbanConfig
