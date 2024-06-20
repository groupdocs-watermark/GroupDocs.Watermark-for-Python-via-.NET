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
        image_search_criteria = gwss.ImageDctHashSearchCriteria(test_files.LogoPng)
        image_search_criteria.max_difference = 0.9

        text_search_criteria = gwss.TextSearchCriteria("Company Name")

        rotate_angle_search_criteria = gwss.RotateAngleSearchCriteria(30.0, 60.0)

        combined_search_criteria = image_search_criteria.or_(text_search_criteria).and_(rotate_angle_search_criteria)

        possible_watermarks = watermarker.search(combined_search_criteria)

        print("\nsearch_watermark_with_combined_search executed successfully.\nFound {0} possible watermark(s).".format(len(possible_watermarks)))

