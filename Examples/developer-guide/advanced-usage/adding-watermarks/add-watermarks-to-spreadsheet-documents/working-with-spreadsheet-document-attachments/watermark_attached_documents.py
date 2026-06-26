import io
from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, Color
from groupdocs.watermark.options.spreadsheet import SpreadsheetLoadOptions

def watermark_attached_documents():
    with Watermarker("./spreadsheet.xlsx", SpreadsheetLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for worksheet in content.worksheets:
            for attachment in worksheet.attachments:
                with Watermarker(io.BytesIO(attachment.content)) as inner:
                    wm = TextWatermark("CONFIDENTIAL", Font("Arial", 19.0))
                    wm.foreground_color = Color.red
                    inner.add(wm)
                    buffer = io.BytesIO()
                    inner.save(buffer)
                # write the watermarked attachment bytes back as needed
        watermarker.save("./output.xlsx")

if __name__ == "__main__":
    watermark_attached_documents()