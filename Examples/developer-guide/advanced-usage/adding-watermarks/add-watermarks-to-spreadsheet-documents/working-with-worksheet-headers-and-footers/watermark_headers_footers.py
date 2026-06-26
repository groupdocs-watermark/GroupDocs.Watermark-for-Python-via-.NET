from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font
from groupdocs.watermark.options.spreadsheet import SpreadsheetLoadOptions

def watermark_headers_footers():
    with Watermarker("./spreadsheet.xlsx", SpreadsheetLoadOptions()) as watermarker:
        watermark = TextWatermark("Protected", Font("Arial", 8.0))
        content = watermarker.get_content()
        for worksheet in content.worksheets:
            for header_footer in worksheet.headers_footers:
                for section in header_footer.sections:
                    if section.image is not None:
                        section.image.add(watermark)
        watermarker.save("./output.xlsx")

if __name__ == "__main__":
    watermark_headers_footers()