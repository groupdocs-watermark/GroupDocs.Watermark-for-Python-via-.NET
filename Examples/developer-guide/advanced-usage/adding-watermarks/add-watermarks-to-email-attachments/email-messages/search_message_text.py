from groupdocs.watermark import Watermarker, WatermarkerSettings
from groupdocs.watermark.search.search_criteria import TextSearchCriteria
from groupdocs.watermark.search.objects import SearchableObjects, EmailSearchableObjects

def search_message_text():
    settings = WatermarkerSettings()
    settings.searchable_objects = SearchableObjects(
        email_searchable_objects=EmailSearchableObjects.SUBJECT | EmailSearchableObjects.PLAIN_TEXT_BODY)

    with Watermarker("./message.msg", settings) as watermarker:
        possible = watermarker.search(TextSearchCriteria("confidential"))
        print("Found", len(possible), "match(es)")

if __name__ == "__main__":
    search_message_text()