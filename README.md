# GroupDocs.Watermark Python Examples - Protect Documents with Watermarks

**Document security** made simple with Python watermarking solutions. This repository contains comprehensive examples demonstrating **how to watermark files**, **add watermark**, **create watermark**, **remove watermark**, and implement **invisible watermarking for documents** using GroupDocs.Watermark for Python via .NET.

## 🔐 Python Document Security & Content Protection

**Protect documents with watermarks** across 40+ file formats with powerful **content protection with watermarking** capabilities:

- **Custom watermark** creation with personalized text and images
- **Customize watermark** appearance, positioning, and transparency
- **Custom fonts** support for branded watermarking solutions
- **Watermark automation for enterprise** Python workflows
- Advanced search and removal capabilities
- **Invisible watermarking for documents** with steganographic techniques
- **Tiling watermarks** across entire document pages for comprehensive coverage

## 📁 Repository Structure

| Directory | Description |
|-----------|-------------|
| [Examples](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/tree/master/Examples) | Complete Python examples showing **how to watermark a** document and implement **document security** |

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
- **How to watermark in** PDF documents with Python
- **Create watermark** with custom fonts and styling
- **Add watermark** to multiple pages simultaneously
- **Customize watermark** transparency and rotation angles

### Advanced Document Security
- **Removing watermark from** third-party applications
- **Delete watermark from** specific document regions
- **Can you remove watermark from** password-protected files
- **How to remove watermarks in** batch processing workflows

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

## 🤝 Support & Community

- [Free Support Forum](https://forum.groupdocs.com/c/watermark) - Get help with **how to remove watermark from free** community
- [Search Documentation](https://search.groupdocs.com/) - Find specific **watermark in** Python solutions
- [Temporary License](https://purchase.groupdocs.com/temporary-license) - Test full features

## 🏷️ Tags

`python-watermarking` `document-security` `content-protection` `pdf-watermark` `document-watermark` `remove-watermark` `add-watermark` `custom-watermark` `enterprise-security` `python-library`

---

**Start securing your Python applications today!** Clone this repository to explore comprehensive examples of **how to watermark a** document, implement **document security**, and leverage **watermark automation for enterprise** Python solutions.

[⬇️ Download Examples](https://github.com/groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET/archive/master.zip) | [🏠 GroupDocs Home](https://www.groupdocs.com/) | [📧 Contact Sales](https://purchase.groupdocs.com/temporary-license)