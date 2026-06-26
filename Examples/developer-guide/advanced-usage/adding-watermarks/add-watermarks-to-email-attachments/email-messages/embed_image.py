from groupdocs.watermark import Watermarker
from groupdocs.watermark.options.email import EmailLoadOptions

def embed_image():
    with Watermarker("./message.msg", EmailLoadOptions()) as watermarker:
        content = watermarker.get_content()
        with open("./logo.png", "rb") as f:
            data = f.read()
        content.embedded_objects.add(data, "logo.png")
        embedded = content.embedded_objects[len(content.embedded_objects) - 1]
        content.html_body = content.html_body.replace(
            "</body>", f'<img src="cid:{embedded.content_id}"/></body>')
        watermarker.save("./output.msg")

if __name__ == "__main__":
    embed_image()