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
        criteria = gwss.TextFormattingSearchCriteria()
        criteria.foreground_color_range = gwss.ColorRange()
        criteria.foreground_color_range.min_hue = -5.0
        criteria.foreground_color_range.max_hue = 10.0
        criteria.foreground_color_range.min_brightness = 0.01
        criteria.foreground_color_range.max_brightness = 0.99
        criteria.background_color_range = gwss.ColorRange()
        criteria.background_color_range.is_empty = True
        criteria.font_name = "Arial"
        criteria.min_font_size = 19.0
        criteria.max_font_size = 42.0
        criteria.font_bold = True

        possible_watermarks = watermarker.search(criteria)
        # The code for working with found watermarks goes here.

        print("\nsearch_watermark_with_particular_text_formatting executed successfully.\nFound {0} possible watermark(s).".format(len(possible_watermarks)))
