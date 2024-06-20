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
        # Initialize criteria with the image
        image_search_criteria = gwss.ImageDctHashSearchCriteria(test_files.LogoPng)

        # Set maximum allowed difference between images
        image_search_criteria.max_difference = 0.9

        possible_watermarks = watermarker.search(image_search_criteria)

        print("\nsearch_image_watermark executed successfully. Found {0} possible watermark(s).".format(len(possible_watermarks)))