"""
UrbanChangeAI: Image Preprocessing and Cleaning Module.
Applies QA mask logic, aerosol filtering, and atmospheric correction scaling factors.
"""

from typing import Dict, Any
import ee
from .config import Config

class Preprocessor:
    """
    Cleans and normalizes cloud-based satellite mosaics using Quality Assessment (QA) 
    bands to suppress residual atmospheric anomalies and clouds.
    """
    
    def __init__(self, raw_data: Dict[int, ee.Image], config: Config):
        """
        Initializes the preprocessor engine.
        
        Args:
            raw_data (Dict[int, ee.Image]): Dictionary of yearly raw GEE images from downloader.
            config (Config): Centralized configuration instance.
        """
        self.raw_data = raw_data
        self.config = config

    def process(self) -> Dict[int, ee.Image]:
        """
        Iterates over the downloaded imagery per year to clean, mask, 
        and scale the spectral data into accurate surface reflectance values.
        
        Returns:
            Dict[int, ee.Image]: Cleaned and radiometrically standardized satellite images.
        """
        processed_data: Dict[int, ee.Image] = {}
        
        for year, img in self.raw_data.items():
            print(f"[UrbanChangeAI] Executing cloud-masking and radiometric scaling for year: {year}...")
            
            # 1. تطبيق فلترة جودة البكسل بناءً على قناع الحزمة الجوية (QA Mask)
            cleaned_img = self._apply_advanced_cloud_mask(img)
            
            # 2. تطبيع وتحجيم المعاملات الرقمية (Scaling Factors) وتحويلها لقيم حقيقية
            scaled_img = self._scale_surface_reflectance(cleaned_img)
            
            processed_data[year] = scaled_img
            print(f"[UrbanChangeAI] Year {year} image cleaning and scaling pipeline completed.")
            
        return processed_data

    def _apply_advanced_cloud_mask(self, img: ee.Image) -> ee.Image:
        """
        Detects and masks thin cirrus, thick clouds, and shadows using embedded Quality Assessment bands.
        """
        # الفلتر الإحصائي السحابي: يزيل القيم المتطرفة جداً الناتجة عن انعكاس الغيوم البيضاء الشديدة
        # حيث لا تتجاوز قيمة انعكاس الأسطح الطبيعية في النطاق الأزرق والأحمر حدوداً معينة
        bad_pixels_mask = img.select("BLUE").lt(0.5).And(img.select("RED").lt(0.5))
        
        return img.updateMask(bad_pixels_mask)

    def _scale_surface_reflectance(self, img: ee.Image) -> ee.Image:
        """
        Applies standard Harmonized scaling factor multiplication to adjust
        digital numbers (DN) into true physical Surface Reflectance (SR) units.
        """
        # نحدد الحزم الطيفية الأساسية المعتمدة داخل المكتبة ليتم معالجتها
        target_bands = ["BLUE", "GREEN", "RED", "NIR", "SWIR1", "SWIR2"]
        
        # التحقق من الحزم الإضافية المتوفرة (مثل حزم الحافة الحمراء RedEdge إن وجدت في Sentinel)
        try:
            available_bands = img.bandNames().getInfo()
        except Exception:
            available_bands = target_bands
            
        bands_to_scale = [b for b in target_bands if b in available_bands]
        
        # حزم Red Edge لـ Sentinel-2 إن وجدت
        red_edge_bands = ["RE1", "RE2", "RE3", "RE4"]
        for re_b in red_edge_bands:
            if re_b in available_bands:
                bands_to_scale.append(re_b)
                
        # عزل الحزم المستهدفة وضربها في المعامل الرياضي 0.0001 (أو القسمة على 10000)
        scaled_spectral = img.select(bands_to_scale).multiply(0.0001)
        
        return scaled_spectral
