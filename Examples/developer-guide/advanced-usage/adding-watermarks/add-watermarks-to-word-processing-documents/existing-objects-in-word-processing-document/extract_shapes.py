from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.word_processing import WordProcessingLoadOptions

def extract_shapes():
    with Watermarker("./document.docx", WordProcessingLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for i, section in enumerate(content.sections):
            print(f"Section {i}: shapes={len(section.shapes)}")
            for shape in section.shapes:
                text = (shape.text or "").strip()
                print(f"  shape text={text!r} size={round(shape.width)}x{round(shape.height)} name={shape.name!r}")

if __name__ == "__main__":
    extract_shapes()