from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, PagesSetup

def add_watermark_to_pages():
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("Test watermark", Font("Arial", 19.0))
        watermark.pages_setup = PagesSetup()
        watermark.pages_setup.pages = [1, 3]
        watermarker.add(watermark)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_watermark_to_pages()