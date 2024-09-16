import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.options.image as gwoi
import groupdocs.watermark.common as gwc
import os
from os.path import join
import test_files
import utils

def run():
    
    # Update with the path to your output directory
    document_path = test_files.sample_tiff
    output_directory = utils.get_output_directory_path()
    output_document_path = join(output_directory, os.path.basename(document_path))

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    load_options = gwoi.TiffImageLoadOptions()
    with gw.Watermarker(document_path, load_options) as watermarker:
        watermark = gww.TextWatermark("Watermark text", gww.Font("Arial", 19.0))
        watermark.foreground_color = gww.Color.red

        watermarker.add(watermark)

        watermarker.save(output_document_path)

    print(f"\nimage_add_watermark executed successfully.\nCheck output in {output_directory}.")
