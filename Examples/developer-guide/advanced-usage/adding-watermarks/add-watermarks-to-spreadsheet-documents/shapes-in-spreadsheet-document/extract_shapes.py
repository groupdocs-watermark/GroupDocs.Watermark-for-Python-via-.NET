from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.spreadsheet import SpreadsheetLoadOptions

def extract_shapes():
    with Watermarker("./spreadsheet.xlsx", SpreadsheetLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for i, worksheet in enumerate(content.worksheets):
            print(f"Worksheet {i}: shapes={len(worksheet.shapes)}")
            for shape in worksheet.shapes:
                text = (shape.text or "").strip()
                print(f"  shape text={text!r} size={round(shape.width)}x{round(shape.height)} "
                      f"word_art={shape.is_word_art}")

if __name__ == "__main__":
    extract_shapes()