from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, Color, SizingType
from groupdocs.watermark.common import HorizontalAlignment, VerticalAlignment

def add_text_watermark():
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("CONFIDENTIAL", Font("Arial", 36.0))
        watermark.foreground_color = Color.red
        watermark.horizontal_alignment = HorizontalAlignment.CENTER
        watermark.vertical_alignment = VerticalAlignment.CENTER
        watermark.sizing_type = SizingType.SCALE_TO_PARENT_DIMENSIONS
        watermark.scale_factor = 0.9
        watermark.rotate_angle = 45.0
        watermark.opacity = 0.5
        watermarker.add(watermark)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_text_watermark()