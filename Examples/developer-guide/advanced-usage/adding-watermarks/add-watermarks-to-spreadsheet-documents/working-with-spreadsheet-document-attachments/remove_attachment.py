from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.spreadsheet import SpreadsheetLoadOptions

def remove_attachment():
    with Watermarker("./spreadsheet.xlsx", SpreadsheetLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for worksheet in content.worksheets:
            for i in range(len(worksheet.attachments) - 1, -1, -1):
                if worksheet.attachments[i].is_link:
                    worksheet.attachments.remove_at(i)
        watermarker.save("./output.xlsx")

if __name__ == "__main__":
    remove_attachment()