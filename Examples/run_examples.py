from quick_start import *
from basic_usage import *
from advanced_usage import *


if __name__ == '__main__':
    ## Quick Start
    set_license_from_file.run()  
    # set_license_from_stream.run()
    # set_metered_license.run()
    hello_world.run()

    ## Basic Usage    
    get_supported_file_formats.run()
    get_document_info.run()
    get_stream_info.run()
    add_text_watermark.run()
    add_image_watermark.run()
   
    # ## Advanced Usage

    ## pdf
    #pdf_add_annotation_watermark.run()
    #pdf_add_artifact_watermark.run()

    ## presentation
    #add_watermark_to_slide.run()

    ## spreadsheet
    #spreadsheet_add_image_watermark_into_header_footer.run()

    ## word
    #word_processing_add_locked_watermark_to_all_pages.run()

    ## loading
    # load_from_local_disk.run()
    # load_document_from_stream.run()
    # load_password_protected_document.run()

    ## searching_modifying
    #modify_text_in_found_watermarks.run()
    #modify_text_with_formatting_in_found_watermarks.run()
    #remove_hyperlinks_with_particular_url.run()
    #search_image_watermark.run()
    #search_watermark_with_particular_text_formatting.run()
    search_watermark.run()
