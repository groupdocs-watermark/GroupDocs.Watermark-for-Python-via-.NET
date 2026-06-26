from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.email import EmailLoadOptions

def remove_attachment():
    with Watermarker("./message.msg", EmailLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for i in range(len(content.attachments) - 1, -1, -1):
            if "sample" in content.attachments[i].name:
                content.attachments.remove_at(i)
        watermarker.save("./output.msg")

if __name__ == "__main__":
    remove_attachment()