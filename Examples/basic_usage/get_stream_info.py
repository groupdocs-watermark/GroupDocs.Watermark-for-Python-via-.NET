import groupdocs.watermark as gw
import test_files

def run():

    with get_file_stream() as stream:
        with gw.Watermarker(stream) as watermarker:
            info = watermarker.get_document_info()

    print("File type: {}".format(info.file_type))
    print("Number of pages: {}".format(info.page_count))
    print("Document size: {} bytes".format(info.size))
 
    print("\nDocument stream info retrieved successfully.")

def get_file_stream():
    file_path = test_files.sample_docx
    return open(file_path, "rb")