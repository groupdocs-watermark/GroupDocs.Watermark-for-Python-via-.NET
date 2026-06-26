from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import ImageWatermark, Color
from groupdocs.watermark.options.word_processing import (
    WordProcessingLoadOptions, WordProcessingWatermarkSectionOptions, WordProcessingImageEffects,
)

def add_watermark_with_effects():
    with Watermarker("./document.docx", WordProcessingLoadOptions()) as watermarker:
        with ImageWatermark("./logo.png") as watermark:
            effects = WordProcessingImageEffects()
            effects.brightness = 0.7
            effects.contrast = 0.6
            effects.chroma_key = Color.red

            options = WordProcessingWatermarkSectionOptions()
            options.name = "Shape 1"
            options.alternative_text = "Company logo watermark"
            options.effects = effects
            watermarker.add(watermark, options)

        watermarker.save("./output.docx")

if __name__ == "__main__":
    add_watermark_with_effects()