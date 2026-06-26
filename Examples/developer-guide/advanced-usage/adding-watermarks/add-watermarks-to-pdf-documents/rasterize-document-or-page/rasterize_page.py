from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.pdf import PdfLoadOptions
from groupdocs.watermark.contents.pdf import PdfImageConversionFormat

def rasterize_page():
    with Watermarker("./document.pdf", PdfLoadOptions()) as watermarker:
        content = watermarker.get_content()
        content.pages[0].rasterize(100, 100, PdfImageConversionFormat.PNG)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    rasterize_page()