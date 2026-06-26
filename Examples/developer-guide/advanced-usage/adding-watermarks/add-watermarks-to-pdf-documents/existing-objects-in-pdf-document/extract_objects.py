from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.pdf import PdfLoadOptions

def extract_objects():
    with Watermarker("./document.pdf", PdfLoadOptions()) as watermarker:
        content = watermarker.get_content()
        page = content.pages[0]
        print(f"Page 1: xobjects={len(page.xobjects)} "
              f"artifacts={len(page.artifacts)} annotations={len(page.annotations)}")
        for artifact in page.artifacts:
            text = (artifact.text or "").strip()
            print(f"  artifact text={text!r} size={round(artifact.width)}x{round(artifact.height)}")
        for annotation in page.annotations:
            text = (annotation.text or "").strip()
            print(f"  annotation text={text!r} size={round(annotation.width)}x{round(annotation.height)}")

if __name__ == "__main__":
    extract_objects()