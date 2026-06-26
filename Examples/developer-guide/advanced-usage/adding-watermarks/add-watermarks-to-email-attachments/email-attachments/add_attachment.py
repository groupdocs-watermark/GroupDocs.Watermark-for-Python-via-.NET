from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.email import EmailLoadOptions

def add_attachment():
    with Watermarker("./message.msg", EmailLoadOptions()) as watermarker:
        content = watermarker.get_content()
        with open("./sample.docx", "rb") as f:
            data = f.read()
        content.attachments.add(data, "sample.docx")
        watermarker.save("./output.msg")

if __name__ == "__main__":
    add_attachment()