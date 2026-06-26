from groupdocs.watermark import Watermarker

def get_document_info():
    with Watermarker("./sample.docx") as watermarker:
        info = watermarker.get_document_info()
        print("File type:", info.file_type)
        print("Pages:", info.page_count)
        print("Size, bytes:", info.size)

if __name__ == "__main__":
    get_document_info()