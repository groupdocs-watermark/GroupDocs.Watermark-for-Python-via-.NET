import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.options.spreadsheet as gwos
import groupdocs.watermark.common as gwc
import os
from os.path import join
import test_files
import utils

def run():
    
    # Update with the path to your output directory
    document_path = test_files.sample_xlsx
    output_directory = utils.get_output_directory_path()
    output_document_path = join(output_directory, os.path.basename(document_path))

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    load_options = gwos.SpreadsheetLoadOptions()
    with gw.Watermarker(document_path, load_options) as watermarker:
        with gww.ImageWatermark(test_files.LogoPng) as watermark:

            options = gwos.SpreadsheetBackgroundWatermarkOptions()
            watermarker.add(watermark, options)

        watermarker.save(output_document_path)

    print(f"\nspreadsheet_add_watermark_as_background executed successfully.\nCheck output in {output_directory}.")
