from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import ImageWatermark, SizingType
from groupdocs.watermark.common import HorizontalAlignment, VerticalAlignment

def add_image_watermark():
    with Watermarker("./sample.docx") as watermarker:
        with ImageWatermark("./logo.png") as watermark:
            watermark.horizontal_alignment = HorizontalAlignment.CENTER
            watermark.vertical_alignment = VerticalAlignment.CENTER
            watermark.sizing_type = SizingType.SCALE_TO_PARENT_DIMENSIONS
            watermark.scale_factor = 0.5
            watermark.opacity = 0.7
            watermarker.add(watermark)
        watermarker.save("./output.docx")

if __name__ == "__main__":
    add_image_watermark()