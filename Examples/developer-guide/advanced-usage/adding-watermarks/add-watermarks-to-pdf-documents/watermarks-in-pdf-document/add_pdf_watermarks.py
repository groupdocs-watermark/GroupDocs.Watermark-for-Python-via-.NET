from groupdocs.watermark import Watermarker
from groupdocs.watermark.watermarks import TextWatermark, ImageWatermark, Font
from groupdocs.watermark.common import HorizontalAlignment, VerticalAlignment
from groupdocs.watermark.options.pdf import (
    PdfLoadOptions, PdfArtifactWatermarkOptions, PdfAnnotationWatermarkOptions,
)

def add_pdf_watermarks():
    with Watermarker("./document.pdf", PdfLoadOptions()) as watermarker:
        # Add as an artifact
        artifact_text = TextWatermark("Artifact", Font("Arial", 8.0))
        artifact_text.horizontal_alignment = HorizontalAlignment.RIGHT
        watermarker.add(artifact_text, PdfArtifactWatermarkOptions())

        # Add as an annotation
        annotation_text = TextWatermark("Annotation", Font("Arial", 8.0))
        annotation_text.horizontal_alignment = HorizontalAlignment.LEFT
        annotation_text.vertical_alignment = VerticalAlignment.TOP
        watermarker.add(annotation_text, PdfAnnotationWatermarkOptions())

        # Add a print-only annotation (visible when printed, hidden on screen)
        with ImageWatermark("./logo.png") as image_watermark:
            image_watermark.horizontal_alignment = HorizontalAlignment.RIGHT
            image_watermark.vertical_alignment = VerticalAlignment.TOP
            options = PdfAnnotationWatermarkOptions()
            options.print_only = True
            watermarker.add(image_watermark, options)

        watermarker.save("./output.pdf")

if __name__ == "__main__":
    add_pdf_watermarks()