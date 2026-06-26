from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font
from groupdocs.watermark.common import HorizontalAlignment, VerticalAlignment

def add_watermark_relative():
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("Test watermark", Font("Calibri", 12.0))
        watermark.horizontal_alignment = HorizontalAlignment.RIGHT
        watermark.vertical_alignment = VerticalAlignment.BOTTOM
        watermark.margins.right = 10
        watermark.margins.bottom = 5
        watermarker.add(watermark)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_watermark_relative()