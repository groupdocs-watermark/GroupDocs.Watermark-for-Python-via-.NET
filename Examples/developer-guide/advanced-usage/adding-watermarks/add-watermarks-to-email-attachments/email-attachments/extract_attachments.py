from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.email import EmailLoadOptions

def extract_attachments():
    with Watermarker("./message.msg", EmailLoadOptions()) as watermarker:
        content = watermarker.get_content()
        print("Attachments:", len(content.attachments))
        for attachment in content.attachments:
            info = attachment.get_document_info()
            print(f"- {attachment.name!r} type={info.file_type}")
            with open(f"./{attachment.name}", "wb") as f:
                f.write(attachment.content)

if __name__ == "__main__":
    extract_attachments()