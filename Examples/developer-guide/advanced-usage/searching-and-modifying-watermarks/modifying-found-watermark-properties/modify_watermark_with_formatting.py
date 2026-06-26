from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import Font, FontStyle, Color
from groupdocs.watermark.search.search_criteria import TextSearchCriteria

def modify_watermark_with_formatting():
    with Watermarker("./watermarked-document.pdf") as watermarker:
        possible = watermarker.search(TextSearchCriteria("CONFIDENTIAL"))
        for wm in possible:
            try:
                wm.formatted_text_fragments.clear()
                wm.formatted_text_fragments.add(
                    "APPROVED",
                    Font("Calibri", 19.0, FontStyle.BOLD),
                    Color.red,
                    Color.aqua,
                )
            except Exception:
                # The entity may not support formatted text, or values may be invalid
                pass
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    modify_watermark_with_formatting()