from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.word_processing import WordProcessingLoadOptions

def unprotect_document():
    with Watermarker("./document.docx", WordProcessingLoadOptions()) as watermarker:
        content = watermarker.get_content()
        content.unprotect()
        watermarker.save("./output.docx")

if __name__ == "__main__":
    unprotect_document()