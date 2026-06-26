from groupdocs.watermark import Watermarker

def remove_watermark():
    with Watermarker("./document.pdf") as watermarker:
        possible = watermarker.search()
        for i in range(len(possible) - 1, -1, -1):
            watermarker.remove(possible[i])
        watermarker.save("./output.pdf")

if __name__ == "__main__":
    remove_watermark()