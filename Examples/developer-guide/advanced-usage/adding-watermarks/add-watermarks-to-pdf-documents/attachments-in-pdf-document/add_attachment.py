from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.pdf import PdfLoadOptions

def add_attachment():
    with Watermarker("./document.pdf", PdfLoadOptions()) as watermarker:
        content = watermarker.get_content()
        with open("./sample.docx", "rb") as f:
            data = f.read()
        content.attachments.add(data, "sample.docx", "Attached Word document")
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_attachment()