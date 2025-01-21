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

    with gw.Watermarker(test_files.sample_pdf_with_watermarks) as watermarker:
        watermarks = watermarker.search()
        for i in range(len(watermarks) - 1, -1, -1):
             print(watermarks[i].text)
             del watermarks[i]

        watermarker.save(join(output_directory, "result.pdf"))

    print(f"\rremove_watermark executed successfully.\nCheck output in {output_directory}.")
