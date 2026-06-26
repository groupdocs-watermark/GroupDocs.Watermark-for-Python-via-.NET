from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.email import EmailLoadOptions

def list_recipients():
    with Watermarker("./message.msg", EmailLoadOptions()) as watermarker:
        content = watermarker.get_content()
        for recipient in list(content.to) + list(content.cc) + list(content.bcc):
            print(recipient.address)

if __name__ == "__main__":
    list_recipients()