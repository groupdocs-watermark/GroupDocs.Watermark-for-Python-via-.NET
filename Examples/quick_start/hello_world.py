import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gwo
import groupdocs.watermark.watermarks as gww
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

    with gw.Watermarker(document_path) as watermarker:
        font = gwo.Font("Arial", 36.0)
        watermark = gwo.TextWatermark("top secret", font)
        watermark.x = 100.0
        watermark.y = 450.0
        watermark.opacity = 0.4
        watermark.rotate_angle = 45.0
        watermark.foreground_color = gww.Color.red
        watermark.is_background = False

        watermarker.add(watermark)
        watermarker.save(join(output_directory, output_document_path))

   
    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nWatermark added successfully.\nCheck output in {output_directory}.")
