from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, Color
from groupdocs.watermark.options.spreadsheet import SpreadsheetLoadOptions

def watermark_worksheet_backgrounds():
    with Watermarker("./spreadsheet.xlsx", SpreadsheetLoadOptions()) as watermarker:
        watermark = TextWatermark("CONFIDENTIAL", Font("Arial", 19.0))
        watermark.foreground_color = Color.red
        content = watermarker.get_content()
        for worksheet in content.worksheets:
            if worksheet.background_image is not None:
                worksheet.background_image.add(watermark)
        watermarker.save("./output.xlsx")

if __name__ == "__main__":
    watermark_worksheet_backgrounds()