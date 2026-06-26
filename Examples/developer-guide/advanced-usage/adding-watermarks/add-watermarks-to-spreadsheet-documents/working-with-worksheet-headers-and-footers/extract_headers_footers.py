from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.spreadsheet import SpreadsheetLoadOptions

def extract_headers_footers():
    with Watermarker("./spreadsheet.xlsx", SpreadsheetLoadOptions()) as watermarker:
        content = watermarker.get_content()
        worksheet = content.worksheets[0]
        print(f"Worksheet 0 header/footer slots: {len(worksheet.headers_footers)}")
        for header_footer in worksheet.headers_footers:
            sections = list(header_footer.sections)
            with_content = [s for s in sections if s.image is not None or s.script]
            print(f"  type={header_footer.header_footer_type} "
                  f"sections={len(sections)} with_content={len(with_content)}")

if __name__ == "__main__":
    extract_headers_footers()