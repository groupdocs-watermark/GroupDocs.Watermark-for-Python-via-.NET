from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.spreadsheet import SpreadsheetLoadOptions

def remove_worksheet_background():
    with Watermarker("./spreadsheet.xlsx", SpreadsheetLoadOptions()) as watermarker:
        content = watermarker.get_content()
        content.worksheets[0].background_image = None
        watermarker.save("./output.xlsx")

if __name__ == "__main__":
    remove_worksheet_background()