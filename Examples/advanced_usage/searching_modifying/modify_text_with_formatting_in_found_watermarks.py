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
        search_criteria = gwss.TextSearchCriteria("test", False)
        watermarks = watermarker.search(search_criteria)
        for watermark in watermarks:
            try:
                # Edit text 
                watermark.formatted_text_fragments.clear()
                watermark.formatted_text_fragments.add(
                    "passed", 
                    gww.Font("Calibri", 19.0, gww.FontStyle.bold), 
                    gww.Color.red, 
                    gww.Color.aqua
                )
            except Exception as e:
                # Found entity may not support text editing
                # Passed arguments can have inappropriate value
                # Process such cases here
                pass

        # Save document
        watermarker.save(join(output_directory, "result.pdf"))

    print(f"\nmodify_text_with_formatting_in_found_watermarks executed successfully.\nCheck output in {output_directory}.")
