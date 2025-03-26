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

    USER_EMAIL = 'useremail@mail.com'
    FILE_ID = '1234-4a04-935f-3c83c3079a47'
    DISCLAIMER = 'Confidential - Do not distribute - Subject to NDA'

    load_options = gwos.SpreadsheetLoadOptions()
    with gw.Watermarker(document_path, load_options) as watermarker:
        font = gww.Font('Helvetica', 12.0)        
        watermark = gww.TextWatermark(f'{USER_EMAIL}\r\n{FILE_ID}\r\n{DISCLAIMER}', font)
        watermark.foreground_color = gww.Color.gray
        watermark.opacity = 0.4
        watermark.rotate_angle = -45.0
        watermark.text_alignment = gww.TextAlignment.CENTER

        options = gwos.SpreadsheetBackgroundWatermarkOptions()
        options.background_width = 200;
        options.background_height = 300;
        
        watermarker.add(watermark, options)

        watermarker.save(output_document_path)

    print(f"\nspreadsheet_add_text_as_background executed successfully.\nCheck output in {output_directory}.")
