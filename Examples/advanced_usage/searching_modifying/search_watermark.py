import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.search as gws
import groupdocs.watermark.search.searchcriteria as gwss
import os
from os.path import join
import test_files
import utils

def run():
    
    print(f"[Example Advanced Usage] # search_watermark\n")

    with gw.Watermarker(test_files.sample_pdf_with_watermarks) as watermarker:
        possible_watermarks = watermarker.search()
        for possible_watermark in possible_watermarks:
            if possible_watermark.image_data is not None:
                print("Image length {0}". format(len(possible_watermark.image_data)))

            print("Text {0}". format(possible_watermark.text))
            print("X {0}". format(possible_watermark.x))
            print("Y {0}". format(possible_watermark.y))
            print("RotateAngle {0}". format(possible_watermark.rotate_angle))
            print("Width {0}". format(possible_watermark.width))
            print("Height {0}". format(possible_watermark.height))
            print("PageNumber {0}". format(possible_watermark.page_number))
            print("")

    print("\nsearch_watermark executed successfully.")