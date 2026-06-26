import os
from groupdocs.watermark import Watermarker, License
from groupdocs.watermark.watermarks import TextWatermark, Font, Color

def add_text_watermark():
    # Optionally set a license
    license_path = os.path.abspath("./GroupDocs.Watermark.lic")
    if os.path.exists(license_path):
        License().set_license(license_path)

    # Open the document, add a text watermark, and save the result
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("CONFIDENTIAL", Font("Arial", 48))
        watermark.foreground_color = Color.red
        watermark.opacity = 0.5
        watermark.rotate_angle = 45.0
        watermarker.add(watermark)
        watermarker.save("./watermarked.pdf")

if __name__ == "__main__":
    add_text_watermark()