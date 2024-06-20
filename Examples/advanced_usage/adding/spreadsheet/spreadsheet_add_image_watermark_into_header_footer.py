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
    output_directory = utils.get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    load_options = gwos.SpreadsheetLoadOptions()
    with gw.Watermarker(test_files.sample_xlsx, load_options) as watermarker:
        with gww.ImageWatermark(test_files.LogoPng) as watermark:
            watermark.vertical_alignment = gwc.VerticalAlignment.TOP
            watermark.horizontal_alignment = gwc.HorizontalAlignment.CENTER
            watermark.sizing_type = gww.SizingType.SCALE_TO_PARENT_DIMENSIONS
            watermark.scale_factor = 1.0

            options = gwos.SpreadsheetWatermarkHeaderFooterOptions()
            options.worksheet_index = 0

            watermarker.add(watermark, options)

        watermarker.save(join(output_directory, "result.xlsx"))

    print(f"\nspreadsheet_add_image_watermark_into_header_footer executed successfully.\nCheck output in {output_directory}.")
