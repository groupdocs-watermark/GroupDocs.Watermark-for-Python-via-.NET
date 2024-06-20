import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.search.searchcriteria as gwss
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
        search_criteria = gwss.TextSearchCriteria("annotation", False)
        watermarks = watermarker.search(search_criteria)
        for watermark in watermarks:
            try:
                # Edit text
                watermark.text = "passed"
            except Exception as e:
                # Found entity may not support text editing
                # Passed argument can have inappropriate value
                # Process such cases here
                pass

        # Save document
        watermarker.save(join(output_directory, "result.pdf"))

    print(f"\nmodify_text_in_found_watermarks executed successfully.\nCheck output in {output_directory}.")
