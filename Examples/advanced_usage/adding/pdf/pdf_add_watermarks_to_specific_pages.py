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
    document_path = test_files.sample_pdf
    output_directory = utils.get_output_directory_path()
    output_document_path = join(output_directory, os.path.basename(document_path))

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    load_options = gwop.PdfLoadOptions()
    with gw.Watermarker(document_path, load_options) as watermarker:
        # Add text watermark
        text_watermark = gww.TextWatermark("This is a test watermark", gww.Font("Arial", 8.0))
        text_watermark.foreground_color = gww.Color.red;
        text_watermark.horizontal_alignment = gwc.HorizontalAlignment.CENTER
        text_watermark.vertical_alignment = gwc.VerticalAlignment.CENTER
        pages_setup = gww.PagesSetup()
        pages_setup.pages = [2,3,4]
        text_watermark.pages_setup = pages_setup
        watermarker.add(text_watermark)

        # Add image watermark to the last page
        with gww.ImageWatermark(test_files.LogoPng) as image_watermark:
            image_watermark.horizontal_alignment = gwc.HorizontalAlignment.RIGHT
            image_watermark.vertical_alignment = gwc.VerticalAlignment.TOP
            pages_setup = gww.PagesSetup()
            pages_setup.last_page = True
            image_watermark.pages_setup = pages_setup
            watermarker.add(image_watermark)

        watermarker.save(output_document_path)

   
    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\pdf_add_watermarks_to_specific_pages executed successfully.\nCheck output in {output_directory}.")
