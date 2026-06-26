from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, Color
from groupdocs.watermark.options.presentation import PresentationLoadOptions

def watermark_slide_backgrounds():
    with Watermarker("./presentation.pptx", PresentationLoadOptions()) as watermarker:
        watermark = TextWatermark("CONFIDENTIAL", Font("Arial", 19.0))
        watermark.foreground_color = Color.red
        content = watermarker.get_content()
        for slide in content.slides:
            if slide.image_fill_format.background_image is not None:
                slide.image_fill_format.background_image.add(watermark)
        watermarker.save("./output.pptx")

if __name__ == "__main__":
    watermark_slide_backgrounds()