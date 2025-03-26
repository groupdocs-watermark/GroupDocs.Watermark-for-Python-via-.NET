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

    USER_EMAIL = 'useremail@mail.com'
    FILE_ID = '1234-4a04-935f-3c83c3079a47'
    DISCLAIMER = 'Confidential - Do not distribute - Subject to NDA'

    with gw.Watermarker(document_path) as watermarker:
        font = gww.Font('Arial', 10.0)
        watermark = gww.TextWatermark(f'{USER_EMAIL}\n{FILE_ID}\n{DISCLAIMER}', font)
        watermark.foreground_color = gww.Color.gray
        watermark.opacity = 0.4
        watermark.rotate_angle = -45.0
        watermark.text_alignment = gww.TextAlignment.CENTER

        line_spacing = gww.MeasureValue()
        line_spacing.measure_type = gww.TileMeasureType.PERCENT
        line_spacing.value = 12.0

        watermark_spacing = gww.MeasureValue()
        watermark_spacing.measure_type = gww.TileMeasureType.PERCENT
        watermark_spacing.value = 10.0

        tile_options = gww.TileOptions()
        tile_options.tile_type = gww.TileType.ONE_THIRD_OFFSET
        tile_options.line_spacing = line_spacing
        tile_options.watermark_spacing = watermark_spacing

        watermark.tile_options = tile_options

        watermarker.add(watermark)
        watermarker.save(output_document_path)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nTile watermark added successfully.\nCheck output in {output_directory}.")
