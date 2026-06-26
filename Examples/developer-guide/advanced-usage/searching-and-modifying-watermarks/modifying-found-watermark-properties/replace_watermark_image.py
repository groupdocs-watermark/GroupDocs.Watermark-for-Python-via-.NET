from groupdocs.watermark import Watermarker
from groupdocs.watermark.search.search_criteria import ImageDctHashSearchCriteria

def replace_watermark_image():
    with open("./stamp.png", "rb") as f:
        image_data = f.read()

    with Watermarker("./watermarked-document.docx") as watermarker:
        criteria = ImageDctHashSearchCriteria("./logo.png")
        criteria.max_difference = 0.9
        possible = watermarker.search(criteria)
        for wm in possible:
            try:
                wm.image_data = image_data
            except Exception:
                # The entity may not support image replacement, or the image format is invalid
                pass
        watermarker.save("./output.docx")

if __name__ == "__main__":
    replace_watermark_image()