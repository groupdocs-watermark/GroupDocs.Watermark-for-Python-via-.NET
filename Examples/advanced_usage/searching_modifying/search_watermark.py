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

    with gw.Watermarker(test_files.sample_docx_with_watermarks) as watermarker:
        possible_watermarks = watermarker.search()
        for possible_watermark in possible_watermarks:
            if possible_watermark.image_data is not None:
                print(len(possible_watermark.image_data))

            print(possible_watermark.text)
            print(possible_watermark.x)
            print(possible_watermark.y)
            print(possible_watermark.rotate_angle)
            print(possible_watermark.width)
            print(possible_watermark.height)