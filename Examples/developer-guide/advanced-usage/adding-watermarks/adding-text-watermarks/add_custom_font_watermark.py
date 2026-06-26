from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font, Color

def add_custom_font_watermark():
    # Point fonts_folder at a directory containing your TrueType (.ttf) fonts
    fonts_folder = r"c:\CustomFonts"
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("Test watermark", Font("CustomFontName", fonts_folder, 36.0))
        watermark.foreground_color = Color.blue
        watermark.opacity = 0.5
        watermark.x = 10
        watermark.y = 10
        watermarker.add(watermark)
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_custom_font_watermark()