# GroupDocs.Watermark Python Examples - Protect Documents with Watermarks

**Document security** made simple with Python watermarking solutions. This repository contains comprehensive examples demonstrating **how to watermark files**, **add watermark**, **create watermark**, **remove watermark**, and implement **invisible watermarking for documents** using GroupDocs.Watermark for Python via .NET.

## 🔐 What You Can Do with GroupDocs.Watermark for Python

**Protect documents with watermarks** across 40+ file formats with powerful **content protection with watermarking** capabilities:

- **Custom watermark** creation with personalized text and images
- **Customize watermark** appearance, positioning, and transparency
- **Custom fonts** support for branded watermarking solutions
- **Watermark automation for enterprise** Python workflows
- Advanced search and removal capabilities
- **Invisible watermarking for documents** with steganographic techniques
- **Tiling watermarks** across entire document pages for comprehensive coverage

## 📁 Repository Structure

| Directory/File | Description |
|----------------|-------------|
| **Examples/** | Root folder containing all example scripts |
| ├── [advanced_usage](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/tree/master/Examples/advanced_usage) | Advanced usage examples demonstrating complex watermarking scenarios |
| ├── [basic_usage](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/tree/master/Examples/basic_usage) | Basic examples for adding, editing, and removing watermarks |
| ├── [quick_start](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/tree/master/Examples/quick_start) | Quick start examples to run and test watermark features immediately |
| ├── [run_examples.py](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/blob/master/Examples/run_examples.py) | Main script to execute all examples |
| ├── [test_files.py](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/blob/master/Examples/test_files.py) | Paths and settings for test files used in examples |
| └── [utils.py](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/blob/master/Examples/utils.py) | Utility functions for handling watermark operations |

## How to run examples

* Call the following command from the root folder of repository   
`python .\Examples\run_examples.py`
* Review rendered files in `.\Examples\Output` folder


## 🚀 Quick Start - How to Watermark Documents in Python

### Installation

Install via pip:
```bash
pip install groupdocs-watermark-net
```

### Add Watermark to Documents

Learn **how to watermark** your documents with this simple Python example:

```python
import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.common as gwс

def run():
  with gw.Watermarker("sample.docx") as watermarker:
      font = gww.Font("Arial", 36.0)
      watermark = gww.TextWatermark("top secret", font)
      watermark.foreground_color = gww.Color.red;
      watermark.horizontal_alignment = gwс.HorizontalAlignment.CENTER
      watermark.vertical_alignment = gwс.VerticalAlignment.CENTER

      watermarker.add(watermark)
      watermarker.save(join(output_directory, "result.docx"))
```

### How to Add Image Watermark 

```python
import groupdocs.watermark as gw
import groupdocs.watermark.watermarks as gww
import groupdocs.watermark.common as gwс

def run():
  with gw.Watermarker("sample.xlsx") as watermarker:
      watermark = gww.ImageWatermark("logo.png")
      watermark.horizontal_alignment = gwс.HorizontalAlignment.CENTER
      watermark.vertical_alignment = gwс.VerticalAlignment.CENTER

      watermarker.add(watermark)
      watermarker.save(join(output_directory, "result.xlsx"))
```

## 📋 Python Watermarking Examples by Use Case

### Basic Watermarking Operations
- [How to watermark in](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/blob/master/Examples/basic_usage/add_text_watermark.py) PDF documents with Python
- [Create watermark](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/blob/master/Examples/basic_usage/add_text_watermark_with_custom_font.py) with custom fonts and styling
- [Add watermark](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/blob/master/Examples/advanced_usage/adding/pdf/pdf_add_watermarks_to_specific_pages.py) to multiple pages simultaneously
- [Customize watermark](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/blob/master/Examples/basic_usage/add_tile_watermark.py) transparency, rotation, and positioning — with the ability to apply tiled watermarks across entire pages for full coverage.

### Advanced Document Security
- [Delete watermark from](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/blob/master/Examples/advanced_usage/searching_modifying/remove_watermark.py) specific document regions
- [Can you remove watermark from](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/blob/master/Examples/advanced_usage/loading/load_password_protected_document.py) password-protected files

### Enterprise Python Solutions
- **Watermark automation for enterprise** document management systems
- **Content protection with watermarking** for sensitive business documents
- **Document security** compliance implementations
- **Customized product** branding with corporate watermarks

## 🎯 Supported File Formats

**How to watermark files** across multiple formats using Python:

**Documents:** PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, RTF  
**Images:** PNG, JPG, BMP, TIFF, GIF, WEBP  
**Email:** EML, MSG, EMLX  
**Other:** Visio files (VSD, VSDX), OpenOffice (ODT)

### System Requirements
- Python 3.6+ 
- .NET runtime (automatically handled via Python.NET)
- Compatible with Windows, macOS, and Linux

## 📖 Documentation & Resources

- [Complete Python API Documentation](https://docs.groupdocs.com/watermark/python-net/)
- [Live Demo - **How to Watermark** Online](https://products.groupdocs.com/watermark/family)
- [Python Package on PyPI](https://pypi.org/project/groupdocs-watermark-net/)
- [Developer Blog](https://blog.groupdocs.com/category/watermark/)

## Relative artilce

- [Python Tiling Watermark Examples: How to Create Repeated Watermarks in Documents](https://blog.groupdocs.com/watermark/tiling-watermark-python/)

## 🤝 Support & Community

- [Free Support Forum](https://forum.groupdocs.com/c/watermark) - Get help with **how to remove watermark from free** community
- [Search Documentation](https://search.groupdocs.com/) - Find specific **watermark in** Python solutions
- [Temporary License](https://purchase.groupdocs.com/temporary-license) - Test full features

## 🏷️ Tags

`python-watermarking` `document-security` `content-protection` `pdf-watermark` `document-watermark` `remove-watermark` `add-watermark` `custom-watermark` `enterprise-security` `python-library`

---

**Start securing your Python applications today!** Clone this repository to explore comprehensive examples of **how to watermark a** document, implement **document security**, and leverage **watermark automation for enterprise** Python solutions.

[⬇️ Download Examples](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/archive/master.zip) | [🏠 GroupDocs Home](https://www.groupdocs.com/) | [📧 Contact Sales](https://purchase.groupdocs.com/temporary-license)