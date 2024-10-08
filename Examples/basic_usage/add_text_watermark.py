import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.common as gwс
import os
from os.path import join
import test_files
import utils

def run():
    
    # Update with the path to your output directory
    document_path = test_files.sample_pdf_2_page
    output_directory = utils.get_output_directory_path()
    output_document_path = join(output_directory, os.path.basename(document_path))

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gw.Watermarker(document_path) as watermarker:
        font = gww.Font("Arial", 36.0)
        watermark = gww.TextWatermark("top secret", font)
        watermark.foreground_color = gww.Color.red;
        watermark.horizontal_alignment = gwс.HorizontalAlignment.CENTER
        watermark.vertical_alignment = gwс.VerticalAlignment.CENTER
        watermark.opacity = 0.4

        pages_setup = gww.PagesSetup()
        pages_setup.pages = [2,3,4]
        watermark.pages_setup = pages_setup

        watermarker.add(watermark)
        watermarker.save(output_document_path)

   
    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nText watermark added successfully.\nCheck output in {output_directory}.")
