from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, Color
from groupdocs.watermark.options.pdf import PdfLoadOptions
from groupdocs.watermark.contents.pdf import PdfImageConversionFormat

def rasterize_document():
    with Watermarker("./document.pdf", PdfLoadOptions()) as watermarker:
        watermark = TextWatermark("CONFIDENTIAL", Font("Arial", 19.0))
        watermark.foreground_color = Color.red
        watermarker.add(watermark)

        # Rasterize every page at 100x100 DPI to PNG images
        content = watermarker.get_content()
        content.rasterize(100, 100, PdfImageConversionFormat.PNG)

        watermarker.save("./output.pdf")

if __name__ == "__main__":
    rasterize_document()