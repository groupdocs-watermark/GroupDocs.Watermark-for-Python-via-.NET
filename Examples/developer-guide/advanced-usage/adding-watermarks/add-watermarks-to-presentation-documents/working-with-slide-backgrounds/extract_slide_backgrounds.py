from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.presentation import PresentationLoadOptions

def extract_slide_backgrounds():
    with Watermarker("./presentation.pptx", PresentationLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for i, slide in enumerate(content.slides):
            background = slide.image_fill_format.background_image
            if background is not None:
                print(f"Slide {i}: background {background.width}x{background.height}")
            else:
                print(f"Slide {i}: no background image")

if __name__ == "__main__":
    extract_slide_backgrounds()