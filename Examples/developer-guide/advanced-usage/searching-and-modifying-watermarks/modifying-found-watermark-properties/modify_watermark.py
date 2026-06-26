from groupdocs.watermark import Watermarker
from groupdocs.watermark.search.search_criteria import TextSearchCriteria

def modify_watermark():
    with Watermarker("./watermarked-document.pdf") as watermarker:
        possible = watermarker.search(TextSearchCriteria("CONFIDENTIAL"))
        for wm in possible:
            try:
                wm.text = "APPROVED"
            except Exception:
                # The entity may not support text editing, or the value is invalid
                pass
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    modify_watermark()