from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, Font
from groupdocs.watermark.common import HorizontalAlignment, VerticalAlignment

def get_add_result():
    with Watermarker("./sample.pdf") as watermarker:
        watermark = TextWatermark("Test watermark", Font("Arial", 19.0))
        watermark.horizontal_alignment = HorizontalAlignment.CENTER
        watermark.vertical_alignment = VerticalAlignment.CENTER

        result = watermarker.add(watermark)
        print("Applied watermarks:", result.number_applied_watermarks)
        for item in result.succeeded:
            print(f"- id={item.watermark_id} type={item.watermark_type} "
                  f"page={item.page_number} position={item.watermark_position}")

if __name__ == "__main__":
    get_add_result()