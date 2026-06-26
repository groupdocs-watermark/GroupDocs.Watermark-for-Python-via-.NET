from groupdocs.watermark import Watermarker

def remove_and_modify_shapes():
    with Watermarker("./diagram.vsdx") as watermarker:
        content = watermarker.get_content()
        for page in content.pages:
            for i in range(len(page.shapes) - 1, -1, -1):
                if page.shapes[i].name == "Rectangle":
                    page.shapes.remove_at(i)
        watermarker.save("./output.vsdx")

if __name__ == "__main__":
    remove_and_modify_shapes()