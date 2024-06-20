import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gwo
import os
from os.path import join
import test_files
import utils

def run():
    
    # Update with the path to your output directory
    output_directory = utils.get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gw.Watermarker(test_files.sample_docx) as watermarker:
        font = gwo.Font("Arial", 36.0)
        watermark = gwo.TextWatermark("top secret", font)
        watermark.x = 100.0;
        watermark.y = 250.0;

        watermarker.add(watermark)
        watermarker.save(join(output_directory, "result.docx"))

   
    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nWatermark added successfully.\nCheck output in {output_directory}.")
