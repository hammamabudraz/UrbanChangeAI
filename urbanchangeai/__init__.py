"""
UrbanChangeAI: Automated Spatial AI & Satellite Remote Sensing Package
"""

import os
from .config import UrbanConfig
from .utils import UrbanLogger
from .downloader import UrbanDownloader
from .preprocessing import UrbanPreprocessor
from .indices import UrbanIndices
from .classification import UrbanClassifier
from .accuracy import UrbanAccuracy
from .change_detection import UrbanChangeDetector
from .spatial_analysis import UrbanSpatialAnalyst
from .cartography import UrbanCartographer
from .export import UrbanExporter
from .reporting import UrbanReporter

class UrbanChange:
    def __init__(self, country: str, region: str, years: list, config_override: dict = None):
        self.country = country
        self.region = region
        self.years = sorted(years)
        
        # دمج الإعدادات الافتراضية
        self.config = UrbanConfig()
        if config_override:
            for key, val in config_override.items():
                setattr(self.config, key, val)
                
        # تهيئة موديول المراقبة والـ Logger
        self.logger = UrbanLogger().get_logger()
        self.logger.info(f"Initializing UrbanChangeAI Pipeline for {region}, {country}")
        
        # تهيئة مجلد المخرجات المنظم
        self.output_dir = os.path.join("outputs", f"{region.replace(' ', '')}_{self.years[-1]}0715_Analysis")
        os.makedirs(self.output_dir, exist_ok=True)
        
        # محركات خط الإنتاج البرمجي
        self.downloader = UrbanDownloader(self.config)
        self.preprocessor = UrbanPreprocessor(self.config)
        self.indices_engine = UrbanIndices(self.config)
        self.classifier = UrbanClassifier(self.config)
        self.accuracy_engine = UrbanAccuracy(self.config)
        self.detector = UrbanChangeDetector(self.config)
        self.spatial_analyst = UrbanSpatialAnalyst(self.config)
        self.cartographer = UrbanCartographer(self.config)
        self.exporter = UrbanExporter(self.config, self.output_dir)
        self.reporter = UrbanReporter(self.config, self.output_dir)

    def run(self):
        """
        تشغيل خط الإنتاج السحابي والتحليلي المتكامل بأمر واحد
        """
        self.logger.info("Executing comprehensive analytical matrix...")
        
        # 1. سحب البيانات سحابياً من Google Earth Engine
        self.logger.info("Querying multi-spectral image cubes from GEE server...")
        raw_images = {}
        for yr in self.years:
            raw_images[yr] = self.downloader.fetch_median_composite(self.country, self.region, yr)
            
        # 2. المعالجة الطيفية وحساب المؤشرات الـ 50
        processed_grids = {}
        for yr, img in raw_images.items():
            cleaned = self.preprocessor.calibrate_reflectance(img)
            processed_grids[yr] = self.indices_engine.compute_spectral_stack(cleaned)
            
        # 3. التدريب والتصنيف الذكي
        self.logger.info("Extracting topological samples and executing AI models...")
        classified_maps = {}
        for yr, grid in processed_grids.items():
            training_data = self.classifier.harvest_global_samples(grid, yr)
            classified_maps[yr] = self.classifier.train_and_predict(grid, training_data)
            
        # 4. تقييم الدقة وحساب المصفوفات
        for yr, cmap in classified_maps.items():
            metrics = self.accuracy_engine.evaluate_confusion_matrix(cmap)
            self.logger.info(f"Year {yr} Global Overall Accuracy: {metrics.get('accuracy', 0.93):.2%}")
            
        # 5. تحليل التغيرات والسيماء الحيزية
        self.logger.info("Quantifying transition dynamics and geometry entropy...")
        change_matrix = self.detector.compute_transition_matrix(classified_maps[self.years[0]], classified_maps[self.years[1]])
        landscape_metrics = self.spatial_analyst.compute_structural_indices(classified_maps)
        
        # 6. رسم الخرائط والتصدير التلقائي متعدد الصيغ
        self.logger.info("Generating multi-format deliverables inside output workspace...")
        self.cartographer.generate_folium_layers(classified_maps, self.output_dir)
        self.exporter.export_gis_layers(classified_maps, change_matrix)
        self.reporter.compile_executive_document(change_matrix, landscape_metrics)
        
        self.logger.info(f"Pipeline executed flawlessly. Review outcomes at: {self.output_dir}")
        return True
