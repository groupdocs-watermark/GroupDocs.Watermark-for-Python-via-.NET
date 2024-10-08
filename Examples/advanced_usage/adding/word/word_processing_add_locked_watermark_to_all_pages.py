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
    document_path = test_files.sample_docx
    output_directory = utils.get_output_directory_path()
    output_document_path = join(output_directory, os.path.basename(document_path))

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    load_options = gwow.WordProcessingLoadOptions()
    with gw.Watermarker(document_path, load_options) as watermarker:
        watermark = gww.TextWatermark("Watermark text", gww.Font("Arial", 19.0))
        watermark.foreground_color = gww.Color.red

        options = gwow.WordProcessingWatermarkPagesOptions()
        options.is_locked = True
        options.lock_type = gwow.WordProcessingLockType.ALLOW_ONLY_FORM_FIELDS

        watermarker.add(watermark, options)

        watermarker.save(output_document_path)

    print(f"\nword_processing_add_locked_watermark_to_all_pages executed successfully.\nCheck output in {output_directory}.")
