import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.common as gwс
import groupdocs.watermark.options as gwo
import os
from os.path import join
import test_files
import utils

def run():
    
    # Update with the path to your output directory
    document_path = test_files.sample_xlsx
    output_directory = utils.get_output_directory_path()
    output_document_path = join(output_directory, os.path.basename(document_path))

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # specifying file type eliminates the need for format detection, enabling faster document opening
    load_options = gwo.LoadOptions()
    load_options.file_type = gwс.FileType.from_extension(os.path.splitext(document_path)[1])

    # Or set the FormatFamily property directly when using a stream, for example:
    #load_options.format_family = gwс.FormatFamily.SPREADSHEET

    with gw.Watermarker(document_path, load_options) as watermarker:
        font = gww.Font("Arial", 36.0)
        watermark = gww.TextWatermark("Test\nwatermark", font)
        watermark.foreground_color = gww.Color.red;
        watermark.horizontal_alignment = gwс.HorizontalAlignment.CENTER
        watermark.vertical_alignment = gwс.VerticalAlignment.CENTER
        watermark.text_alignment = gww.TextAlignment.CENTER;

        watermarker.add(watermark)
        watermarker.save(output_document_path)

   
    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nload_document_with_known_type executed successfully.\nCheck output in {output_directory}.")
