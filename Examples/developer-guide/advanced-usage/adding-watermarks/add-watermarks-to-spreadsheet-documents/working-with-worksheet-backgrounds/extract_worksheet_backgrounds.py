from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.spreadsheet import SpreadsheetLoadOptions

def extract_worksheet_backgrounds():
    with Watermarker("./spreadsheet.xlsx", SpreadsheetLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for i, worksheet in enumerate(content.worksheets):
            background = worksheet.background_image
            if background is not None:
                print(f"Worksheet {i}: background {background.width}x{background.height}")
            else:
                print(f"Worksheet {i}: no background")

if __name__ == "__main__":
    extract_worksheet_backgrounds()