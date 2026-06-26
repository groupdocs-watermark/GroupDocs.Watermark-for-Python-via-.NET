from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, MarginType
from groupdocs.watermark.common import HorizontalAlignment, VerticalAlignment

def add_watermark_margin_type():
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("Test watermark", Font("Calibri", 12.0))
        watermark.horizontal_alignment = HorizontalAlignment.RIGHT
        watermark.vertical_alignment = VerticalAlignment.BOTTOM
        watermark.margins.margin_type = MarginType.RELATIVE_TO_PARENT_DIMENSIONS
        watermark.margins.right = 0.1
        watermark.margins.bottom = 0.2
        watermarker.add(watermark)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_watermark_margin_type()