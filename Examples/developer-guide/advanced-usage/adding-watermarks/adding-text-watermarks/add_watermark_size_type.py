from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, SizingType

def add_watermark_size_type():
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("This is a test watermark", Font("Calibri", 12.0))
        watermark.sizing_type = SizingType.SCALE_TO_PARENT_DIMENSIONS
        watermark.scale_factor = 0.5
        watermarker.add(watermark)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_watermark_size_type()