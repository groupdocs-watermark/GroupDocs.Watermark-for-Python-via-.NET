# import groupdocs.watermark as gw
# import groupdocs.watermark.watermarks as gww
# import groupdocs.watermark.options as gwo
# import os
# from os.path import join
# import test_files
# import utils

# def run():
    
#     # Update with the path to your output directory
#     output_directory = utils.get_output_directory_path()

#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)

#     def create_page_stream_delegate(number):
#         preview_image_file_name = os.path.join(output_directory, f"page{number}.png")
#         return open(preview_image_file_name, 'wb')

#     def release_page_stream_delegate(number, stream):
#         stream.close()

#     with gw.Watermarker(test_files.InPresentationPptx) as watermarker:
#         preview_options = gwo.PreviewOptions(create_page_stream_delegate, release_page_stream_delegate)
#         watermarker.generate_preview(preview_options)
   
#     # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
#     print(f"\Dcoument preview generated successfully.\nCheck output in {output_directory}.")
