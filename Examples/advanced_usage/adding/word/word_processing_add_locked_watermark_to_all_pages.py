import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.options.wordprocessing as gwow
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

    load_options = gwow.WordProcessingLoadOptions()
    with gw.Watermarker(test_files.sample_docx, load_options) as watermarker:
        watermark = gww.TextWatermark("Watermark text", gww.Font("Arial", 19.0))
        watermark.foreground_color = gww.Color.red

        options = gwow.WordProcessingWatermarkPagesOptions()
        options.is_locked = True
        options.lock_type = gwow.WordProcessingLockType.ALLOW_ONLY_FORM_FIELDS

        watermarker.add(watermark, options)

        watermarker.save(join(output_directory, "result.docx"))

    print(f"\nword_processing_add_locked_watermark_to_all_pages executed successfully.\nCheck output in {output_directory}.")
