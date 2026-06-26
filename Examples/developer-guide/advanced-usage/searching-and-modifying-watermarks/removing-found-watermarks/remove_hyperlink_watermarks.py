import re
from groupdocs.watermark import Watermarker
from groupdocs.watermark.search import HyperlinkPossibleWatermark
from groupdocs.watermark.search.search_criteria import TextSearchCriteria

def remove_hyperlink_watermarks():
    with Watermarker("./document.pdf") as watermarker:
        possible = watermarker.search(TextSearchCriteria(re.compile(r"someurl\.com")))
        for i in range(len(possible) - 1, -1, -1):
            if isinstance(possible[i], HyperlinkPossibleWatermark):
                print(possible[i].text)
                watermarker.remove(possible[i])
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    remove_hyperlink_watermarks()