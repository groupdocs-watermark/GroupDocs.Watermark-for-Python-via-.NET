from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.spreadsheet import SpreadsheetLoadOptions

def extract_attachments():
    with Watermarker("./spreadsheet.xlsx", SpreadsheetLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for i, worksheet in enumerate(content.worksheets):
            for attachment in worksheet.attachments:
                info = attachment.get_document_info()
                print(f"Worksheet {i}: {attachment.alternative_text!r} type={info.file_type}")
                with open(f"./{attachment.alternative_text}", "wb") as f:
                    f.write(attachment.content)

if __name__ == "__main__":
    extract_attachments()