import groupdocs.watermark as gw
import test_files

def run():

    with gw.Watermarker(test_files.sample_docx) as watermarker:
        info = watermarker.get_document_info()

    print("File type: {}".format(info.file_type))
    print("Number of pages: {}".format(info.page_count))
    print("Document size: {} bytes".format(info.size))

   
    print("\nDocument info retrieved successfully.")
