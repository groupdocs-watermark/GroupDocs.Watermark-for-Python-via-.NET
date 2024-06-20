import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.options as gwo
import os
from os.path import join
import test_files
import utils

def run():
    
    # Update with the path to your output directory
    output_directory = utils.get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    load_options = gwo.LoadOptions()
    load_options.password = "P@$$w0rd"
    with gw.Watermarker(test_files.sample_docx_with_password, load_options) as watermarker:
        # use watermarker methods to manage watermarks in the document
        watermark = gww.TextWatermark("Test watermark", gww.Font("Arial", 12.0))

        watermarker.add(watermark)
        watermarker.save(join(output_directory, "result.docx"))

    print(f"\nload_password_protected_document executed successfully.\nCheck output in {output_directory}.")
