from groupdocs.watermark.common import FileType

def list_supported_formats():
    # Enumerate every file type the library can open
    supported_file_types = FileType.get_supported_file_types()
    for file_type in sorted(supported_file_types, key=lambda x: x.extension):
        print(file_type)

if __name__ == "__main__":
    list_supported_formats()