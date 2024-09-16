# test_files.py
# This module defines paths to test files.

import os
from os.path import join
import platform
import utils

def get_sample_file_path(file_path):
    if platform.system() == 'Windows':
        return join(utils.samples_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, utils.samples_path, file_path)

fonts_path = utils.fonts_path

# PDFs
sample_pdf = get_sample_file_path("sample.pdf")
sample_pdf_2_page = get_sample_file_path("sample 2p.pdf")
sample_pdf_with_watermarks = get_sample_file_path("document with watermarks.pdf")

# Presentations
InPresentationPptx = get_sample_file_path("sample.pptx")

# Visio files
sample_visio = get_sample_file_path("sample.vsdx")

# Spreadsheets
sample_xlsx = get_sample_file_path("sample.xlsx")

# Word Processing documents
sample_docx = get_sample_file_path("sample.docx")
sample_docx_with_password = get_sample_file_path("protected-document.docx")
sample_docx_with_watermarks = get_sample_file_path("document with watermarks.docx")

sample_tiff = get_sample_file_path("sample.tiff")

# Graphics
LogoPng = get_sample_file_path("logo.png")



    