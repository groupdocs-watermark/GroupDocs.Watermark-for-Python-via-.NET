from groupdocs.watermark import Watermarker

def extract_shapes():
    with Watermarker("./diagram.vsdx") as watermarker:
        content = watermarker.get_content()
        page = content.pages[0]
        print(f"Pages: {len(content.pages)}; page 1 shapes: {len(page.shapes)}")
        for shape in page.shapes:
            text = (shape.text or "").strip()
            print(f"  shape name={shape.name!r} text={text!r} "
                  f"size={round(shape.width)}x{round(shape.height)}")

if __name__ == "__main__":
    extract_shapes()