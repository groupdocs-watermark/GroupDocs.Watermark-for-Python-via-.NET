import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.options.presentation as gwop
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

    load_options = gwop.PresentationLoadOptions()
    with gw.Watermarker(test_files.InPresentationPptx, load_options) as watermarker:
        # Add text watermark to the first slide
        text_watermark = gww.TextWatermark("Test watermark", gww.Font("Arial", 8.0))
        text_watermark_options = gwop.PresentationWatermarkSlideOptions()
        text_watermark_options.slide_index = 0
        watermarker.add(text_watermark, text_watermark_options)

        # Add image watermark to the second slide
        with gww.ImageWatermark(test_files.LogoPng) as image_watermark:
            image_watermark_options = gwop.PresentationWatermarkSlideOptions()
            image_watermark_options.slide_index = 1
            watermarker.add(image_watermark, image_watermark_options)

        watermarker.save(join(output_directory, "result.pptx"))

    print(f"\nadd_watermark_to_slide executed successfully.\nCheck output in {output_directory}.")
