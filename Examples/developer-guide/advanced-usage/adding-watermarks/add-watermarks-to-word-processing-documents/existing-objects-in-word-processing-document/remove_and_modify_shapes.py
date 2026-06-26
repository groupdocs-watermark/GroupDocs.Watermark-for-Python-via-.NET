from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.word_processing import WordProcessingLoadOptions

def remove_and_modify_shapes():
    with Watermarker("./document.docx", WordProcessingLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for section in content.sections:
            for i in range(len(section.shapes) - 1, -1, -1):
                if section.shapes[i].text == "CONFIDENTIAL":
                    section.shapes.remove_at(i)
        watermarker.save("./output.docx")

if __name__ == "__main__":
    remove_and_modify_shapes()