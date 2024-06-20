# get_supported_file_formats.py
# This examples demonstrates how to print out all supported file types.

import groupdocs.watermark.common as gw

def run():
    supported_file_types = gw.FileType.get_supported_file_types()

    for file_type in sorted(supported_file_types, key=lambda x: x.extension):
        print(file_type)

    print("\nSupported file types retrieved successfully.")
