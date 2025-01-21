import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.search as gws
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
        watermarks = watermarker.search(gwss.TextSearchCriteria("someurl.com"))
        for i in range(len(watermarks) - 1, -1, -1):
            # Ensure that only hyperlinks will be removed
            if isinstance(watermarks[i], gws.HyperlinkPossibleWatermark):
                # Output the full url of the hyperlink
                print(watermarks[i].text)

                # Remove hyperlink from the document
                del watermarks[i]

        watermarker.save(join(output_directory, "result.pdf"))

    print(f"\nremove_hyperlinks_with_particular_url executed successfully.\nCheck output in {output_directory}.")
