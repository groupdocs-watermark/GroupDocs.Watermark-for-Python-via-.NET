import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.options.pdf as gwop
import groupdocs.watermark.common as gwc
import groupdocs.watermark.contents.pdf as gwcp
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
    with gw.Watermarker(test_files.sample_pdf_with_watermarks, load_options) as watermarker:
        pdf_content = watermarker.get_content(gwcp.PdfContent)
        for page in pdf_content.pages:
            for annotation in page.annotations:
                print(annotation.annotation_type)
                if annotation.image is not None:
                    print(annotation.image.width)
                    print(annotation.image.height)
                    print(len(annotation.image.get_bytes()))

                print(annotation.text)
                print(annotation.x)
                print(annotation.y)
                print(annotation.width)
                print(annotation.height)
                print(annotation.rotate_angle)
    
    print(f"\npdf_extract_annotation_information executed successfully.\nCheck output in {output_directory}.")
