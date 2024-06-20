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
    watermark = gww.TextWatermark("This is WaterMark on Attachment", gww.Font("Arial", 19.0))
    with gw.Watermarker(test_files.sample_pdf_with_watermarks, load_options) as watermarker:
        pdf_content = watermarker.get_content(gwcp.PdfContent)
        for attachment in pdf_content.attachments:
            # Check if the attached file is supported by GroupDocs.Watermark
            info = attachment.get_document_info()
            if info.file_type != gwc.FileType.UNKNOWN and not info.is_encrypted:
                # Load the attached document
                with attachment.create_watermarker() as attached_watermarker:
                    # Add watermark
                    attached_watermarker.add(watermark)

                    # Save changes in the attached file
                    attached_watermarker.save()

        watermarker.save(join(output_directory, "result.pdf"))

    print(f"\npdf_add_watermark_to_all_attachments executed successfully.\nCheck output in {output_directory}.")
