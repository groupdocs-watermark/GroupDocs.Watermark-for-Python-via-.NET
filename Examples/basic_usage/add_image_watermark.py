import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.common as gwс
import os
from os.path import join
import test_files
import utils

def run():
    
    # Update with the path to your output directory
    output_directory = utils.get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gw.Watermarker(test_files.sample_xlsx) as watermarker:
        watermark = gww.ImageWatermark(test_files.LogoPng)
        watermark.horizontal_alignment = gwс.HorizontalAlignment.CENTER
        watermark.vertical_alignment = gwс.VerticalAlignment.CENTER

        watermarker.add(watermark)
        watermarker.save(join(output_directory, "result.xlsx"))

   
    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\Image watermark added successfully.\nCheck output in {output_directory}.")
