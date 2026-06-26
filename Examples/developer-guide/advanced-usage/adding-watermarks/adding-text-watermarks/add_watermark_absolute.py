from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font

def add_watermark_absolute():
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("Test watermark", Font("Times New Roman", 8.0))
        watermark.x = 10
        watermark.y = 20
        watermark.width = 100
        watermark.height = 40
        watermarker.add(watermark)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_watermark_absolute()