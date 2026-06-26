from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, Color, SizingType
from groupdocs.watermark.common import HorizontalAlignment, VerticalAlignment

def add_watermark_parent_margins():
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("Test watermark", Font("Arial", 42.0))
        watermark.horizontal_alignment = HorizontalAlignment.RIGHT
        watermark.vertical_alignment = VerticalAlignment.TOP
        watermark.sizing_type = SizingType.SCALE_TO_PARENT_DIMENSIONS
        watermark.scale_factor = 1.0
        watermark.rotate_angle = 45
        watermark.foreground_color = Color.red
        watermark.background_color = Color.aqua
        watermark.consider_parent_margins = True
        watermarker.add(watermark)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_watermark_parent_margins()