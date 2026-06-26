import os
from groupdocs.watermark import Watermarker, License
from groupdocs.watermark.watermarks import ImageWatermark

def add_image_watermark():
    # Optionally set a license
    license_path = os.path.abspath("./GroupDocs.Watermark.lic")
    if os.path.exists(license_path):
        License().set_license(license_path)

    # Open the document, add an image watermark, and save the result
    with Watermarker("./sample.docx") as watermarker:
        watermark = ImageWatermark("./logo.png")
        watermark.opacity = 0.5
        watermarker.add(watermark)
        watermarker.save("./watermarked.docx")

if __name__ == "__main__":
    add_image_watermark()