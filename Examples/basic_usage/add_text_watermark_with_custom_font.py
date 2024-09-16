import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.common as gwс
import os
from os.path import join
import test_files
import utils

def run():
    
    # Update with the path to your output directory
    document_path = test_files.sample_pdf
    output_directory = utils.get_output_directory_path()
    output_document_path = join(output_directory, os.path.basename(document_path))
    fonts_folder = test_files.fonts_path

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gw.Watermarker(document_path) as watermarker:
        font = gww.Font("OT Chekharda Bold Italic", fonts_folder, 36.0)
        watermark = gww.TextWatermark("top secret", font)
        watermark.foreground_color = gww.Color.red;
        watermark.opacity = 0.4
        watermark.x = 10.0
        watermark.y = 500.0
            
        watermarker.add(watermark)
        watermarker.save(output_document_path)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nText watermark with custom font added successfully.\nCheck output in {output_directory}.")
