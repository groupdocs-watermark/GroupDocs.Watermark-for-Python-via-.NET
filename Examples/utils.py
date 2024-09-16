# utils.py
# This module provides utility functions and constants.

import os
from os.path import join
import inspect

resources_path = "./Resources"
samples_path = "./Resources/SampleFiles"
fonts_path = "./Resources/Fonts"
output_path = "./Output"
license_path = join(resources_path, "Conholdate.Total.Product.Family.lic")

def get_output_directory_path():
    caller_frame = inspect.currentframe().f_back
    caller_file_path = caller_frame.f_globals.get("__file__")
    caller_file_name = os.path.basename(caller_file_path)
    output_directory = join(output_path, os.path.splitext(caller_file_name)[0])

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    return os.path.abspath(output_directory)
