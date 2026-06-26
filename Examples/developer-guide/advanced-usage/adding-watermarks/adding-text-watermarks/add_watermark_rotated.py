from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, SizingType
from groupdocs.watermark.common import HorizontalAlignment, VerticalAlignment

def add_watermark_rotated():
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("Test watermark", Font("Calibri", 8.0))
        watermark.horizontal_alignment = HorizontalAlignment.RIGHT
        watermark.vertical_alignment = VerticalAlignment.TOP
        watermark.sizing_type = SizingType.SCALE_TO_PARENT_DIMENSIONS
        watermark.scale_factor = 0.5
        watermark.rotate_angle = 45
        watermarker.add(watermark)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_watermark_rotated()