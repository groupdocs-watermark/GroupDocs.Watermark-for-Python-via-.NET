from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.pdf import PdfLoadOptions

def remove_and_modify_objects():
    with Watermarker("./document.pdf", PdfLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for page in content.pages:
            for i in range(len(page.artifacts) - 1, -1, -1):
                if page.artifacts[i].text and "watermark" in page.artifacts[i].text.lower():
                    page.artifacts.remove_at(i)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    remove_and_modify_objects()