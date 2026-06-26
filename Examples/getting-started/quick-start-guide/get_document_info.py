import os
from groupdocs.watermark import Watermarker, License

def get_document_info():
    # Optionally set a license
    license_path = os.path.abspath("./GroupDocs.Watermark.lic")
    if os.path.exists(license_path):
        License().set_license(license_path)

    # Open the document and read its metadata
    with Watermarker("./sample.pdf") as watermarker:
        info = watermarker.get_document_info()

        print("File type:", info.file_type)
        print("Pages:", info.page_count)
        print("Size, bytes:", info.size)

if __name__ == "__main__":
    get_document_info()