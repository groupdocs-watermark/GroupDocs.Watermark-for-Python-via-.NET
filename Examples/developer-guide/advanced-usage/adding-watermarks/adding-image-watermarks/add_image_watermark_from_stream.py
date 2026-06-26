import io
from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import ImageWatermark

def add_image_watermark_from_stream():
    with open("./logo.png", "rb") as f:
        data = f.read()

    with Watermarker("./sample.docx") as watermarker:
        with ImageWatermark(stream=io.BytesIO(data)) as watermark:
            watermarker.add(watermark)
        watermarker.save("./output.docx")

if __name__ == "__main__":
    add_image_watermark_from_stream()