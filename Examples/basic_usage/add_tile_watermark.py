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

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gw.Watermarker(document_path) as watermarker:
        font = gww.Font("Arial", 36.0)
        watermark = gww.TextWatermark("top secret", font)
        watermark.foreground_color = gww.Color.red;
        watermark.opacity = 0.4
        watermark.rotate_angle = 45.0

        line_spacing = gww.MeasureValue()
        line_spacing.measure_type = gww.TileMeasureType.PERCENT
        line_spacing.value = 12.0

        watermark_spacing = gww.MeasureValue()
        watermark_spacing.measure_type = gww.TileMeasureType.PERCENT
        watermark_spacing.value = 10.0

        watermark.tile_options = gww.TileOptions()
        watermark.tile_options.line_spacing = line_spacing
        watermark.tile_options.watermark_spacing = watermark_spacing
            
        watermarker.add(watermark)
        watermarker.save(output_document_path)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nTile watermark added successfully.\nCheck output in {output_directory}.")
