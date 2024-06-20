import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.options.pdf as gwop
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

    load_options = gwop.PdfLoadOptions()
    with gw.Watermarker(test_files.sample_pdf, load_options) as watermarker:
        options = gwop.PdfAnnotationWatermarkOptions()

        # Add text watermark
        text_watermark = gww.TextWatermark("This is a annotation watermark", gww.Font("Arial", 8.0))
        text_watermark.horizontal_alignment = gwc.HorizontalAlignment.LEFT
        text_watermark.vertical_alignment = gwc.VerticalAlignment.TOP
        watermarker.add(text_watermark, options)

        # Add image watermark
        with gww.ImageWatermark(test_files.LogoPng) as image_watermark:
            image_watermark.horizontal_alignment = gwc.HorizontalAlignment.RIGHT
            image_watermark.vertical_alignment = gwc.VerticalAlignment.TOP
            watermarker.add(image_watermark, options)

        watermarker.save(join(output_directory, "result.pdf"))

   
    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\Watermark added successfully.\nCheck output in {output_directory}.")
