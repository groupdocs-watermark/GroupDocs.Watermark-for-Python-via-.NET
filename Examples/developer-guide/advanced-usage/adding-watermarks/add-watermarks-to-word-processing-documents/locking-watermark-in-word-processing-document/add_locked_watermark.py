from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, Color
from groupdocs.watermark.options.word_processing import (
    WordProcessingLoadOptions, WordProcessingWatermarkSectionOptions, WordProcessingLockType,
)

def add_locked_watermark():
    with Watermarker("./document.docx", WordProcessingLoadOptions()) as watermarker:
        watermark = TextWatermark("CONFIDENTIAL", Font("Arial", 19.0))
        watermark.foreground_color = Color.red

        options = WordProcessingWatermarkSectionOptions()
        options.is_locked = True
        options.lock_type = WordProcessingLockType.ALLOW_ONLY_FORM_FIELDS
        # options.password = "p@ssw0rd"   # optional
        watermarker.add(watermark, options)

        watermarker.save("./output.docx")

if __name__ == "__main__":
    add_locked_watermark()