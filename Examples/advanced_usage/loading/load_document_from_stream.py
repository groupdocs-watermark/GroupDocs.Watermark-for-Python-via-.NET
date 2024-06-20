import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import os
from os.path import join
import test_files
import utils

def run():
    
    # Update with the path to your output directory
    output_directory = utils.get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with get_file_stream() as stream:
        with gw.Watermarker(stream) as watermarker:
            # use watermarker methods to manage watermarks
            watermark = gww.TextWatermark("Test watermark", gww.Font("Arial", 12.0))

            watermarker.add(watermark)
            watermarker.save(join(output_directory, "result.docx"))

    print(f"\nload_document_from_stream executed successfully.\nCheck output in {output_directory}.")

def get_file_stream():
    file_path = test_files.sample_docx
    return open(file_path, "rb")