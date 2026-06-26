from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import ImageWatermark
from groupdocs.watermark.common import HorizontalAlignment, VerticalAlignment

def add_image_watermark():
    with Watermarker("./sample.docx") as watermarker:
        # Build an image watermark from a logo file and center it
        watermark = ImageWatermark("./logo.png")
        watermark.horizontal_alignment = HorizontalAlignment.CENTER
        watermark.vertical_alignment = VerticalAlignment.CENTER
        watermark.opacity = 0.7

        watermarker.add(watermark)
        watermarker.save("./output.docx")

if __name__ == "__main__":
    add_image_watermark()