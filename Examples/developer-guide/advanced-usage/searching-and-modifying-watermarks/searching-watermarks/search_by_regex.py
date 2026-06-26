import re
from groupdocs.watermark import Watermarker
from groupdocs.watermark.search.search_criteria import TextSearchCriteria

def search_by_regex():
    with Watermarker("./document.pdf") as watermarker:
        possible = watermarker.search(TextSearchCriteria(re.compile(r"^CONFIDENTIAL$")))
        print("Found", len(possible), "possible watermark(s)")

if __name__ == "__main__":
    search_by_regex()