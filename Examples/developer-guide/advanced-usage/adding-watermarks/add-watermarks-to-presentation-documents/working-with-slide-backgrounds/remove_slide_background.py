from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.presentation import PresentationLoadOptions

def remove_slide_background():
    with Watermarker("./presentation.pptx", PresentationLoadOptions()) as watermarker:
        content = watermarker.get_content()
        content.slides[0].image_fill_format.background_image = None
        watermarker.save("./output.pptx")

if __name__ == "__main__":
    remove_slide_background()