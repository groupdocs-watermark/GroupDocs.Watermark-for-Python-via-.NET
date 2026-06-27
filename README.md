# GroupDocs.Watermark for Python via .NET - Code Examples

[![banner](https://raw.githubusercontent.com/groupdocs/groupdocs.github.io/master/img/banners/groupdocs-watermark-python-net-banner.png)](https://releases.groupdocs.com/watermark/python-net/)

[Product Page](https://products.groupdocs.com/watermark/python-net/) | [Docs](https://docs.groupdocs.com/watermark/python-net/) | [Demos](https://products.groupdocs.app/watermark/family) | [API Reference](https://reference.groupdocs.com/watermark/python-net/) | [Blog](https://blog.groupdocs.com/category/watermark/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/watermark) | [Temporary License](https://purchase.groupdocs.com/temporary-license)

[GroupDocs.Watermark for Python via .NET](https://products.groupdocs.com/watermark/python-net/) adds, searches, and removes text and image watermarks across PDF, Word, Excel, PowerPoint, Visio, email, and image formats through one unified API — style and position watermarks, tile them across a page, lock them, target specific pages or slides, and search or remove existing watermarks — all on-premise, with no MS Office or OpenOffice installation required.

## Features

- **Text & Image Watermarks**: Add styled text or image watermarks with configurable color, opacity, rotation, alignment, and sizing.
- **Custom Fonts**: Load and apply custom fonts for branded watermarks.
- **Tiled Watermarks**: Repeat a watermark across an entire page for full coverage.
- **Format-Specific Placement**: PDF annotations/artifacts, presentation slides, Visio pages, spreadsheet backgrounds and header/footers, and locked Word watermarks.
- **Page Targeting**: Apply watermarks to specific pages or the last page only.
- **Search & Modify**: Find watermarks by text, image similarity, or formatting; edit their text or remove them.
- **On-Premise**: No MS Office or OpenOffice installation required.

## Supported File Formats

GroupDocs.Watermark for Python via .NET supports a wide range of file formats, including Word, Excel, PowerPoint, PDF, OpenDocument, Visio, email, and image formats. See the [full list of supported formats](https://docs.groupdocs.com/watermark/python-net/getting-started/supported-document-formats/) for details.

## Get Started

1. **Set Up Environment**: Ensure that [Python 3.5+](https://www.python.org/downloads/) is installed on your system.

2. **Get the Code**: Clone or download this repository.

   ```bash
   git clone git@github.com:groupdocs-watermark/GroupDocs.Watermark-for-Python-via-.NET.git
   ```

3. **Navigate to the `Examples` Folder**

   ```bash
   cd ./GroupDocs.Watermark-for-Python-via-.NET/Examples
   ```

4. **Install Package**: install dependencies with pip:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, download the platform-specific `.whl` file from the [GroupDocs Releases](https://releases.groupdocs.com/watermark/python-net/) website and install it directly (adjust the filename to your platform — `win_amd64`, `manylinux*_x86_64`, `macosx_*_arm64`, `macosx_*_x86_64`):

   ```bash
   pip install ./groupdocs_watermark_net-26.6.0-py3-none-win_amd64.whl
   ```

5. **Configure License (Optional)**: examples run with the full feature set when a license is available, looking in two places:

   - The `GROUPDOCS_LIC_PATH` environment variable — set it to the absolute path of your `.lic` file (recommended; the package auto-applies it at import).
   - A license applied explicitly in code via `License().set_license(...)`.

   Without a license, the library runs in evaluation mode (the output is watermarked and only the first watermark per document is kept). Get a free 30-day [temporary license](https://purchase.groupdocs.com/temporary-license) for evaluation.

6. **Run the Examples**: To run all the examples, execute the following command:

   ```bash
   python ./run_all_examples.py
   ```

   Each example runs in its own subprocess with paths relative to its own folder, so output files are placed next to the example script. You can also run an individual example by navigating to its folder and running the script directly.

## Project Structure

```
Examples/
├── run_all_examples.py     # Runs every example and prints a pass/fail summary
├── _run_example.py         # Per-example wrapper (applies license, isolates eval limits)
├── requirements.txt
├── licensing/              # Set a license from a file, a stream, or a metered key
├── getting-started/
│   └── hello-world/        # Minimal add-a-watermark example
└── developer-guide/
    ├── basic-usage/        # Add text/image/custom-font/tile watermarks, document info, formats
    └── advanced-usage/     # Loading options, format-specific placement, search & modify
```

## Run with Docker

The repository ships a `Dockerfile` that builds a Linux image with Python 3.13, the .NET runtime dependencies (`libicu-dev`, `libgdiplus`, `libfontconfig1`), and the `groupdocs-watermark-net` package preinstalled.

```bash
# Build the image
docker build -t watermark-examples .

# Run unlicensed (evaluation mode)
docker run --rm watermark-examples

# Run with a license mounted from the host
docker run --rm \
    -v /path/to/license:/lic:ro \
    -e GROUPDOCS_LIC_PATH=/lic/your-license.lic \
    watermark-examples
```

On Windows with Git Bash, set `export MSYS_NO_PATHCONV=1` before `docker run` to prevent MSYS from rewriting the mounted license path.

## AI agents and LLM integration

The `groupdocs-watermark-net` wheel ships a bundled `AGENTS.md` reference for AI coding assistants (Claude Code, Cursor, GitHub Copilot in agent mode, and similar). Once the package is installed, the reference is discovered automatically at `groupdocs/watermark/AGENTS.md` — it covers canonical imports, quick-start usage, licensing, the API surface table, and troubleshooting. A copy also lives in this repository's root [`AGENTS.md`](./AGENTS.md).

For on-demand documentation lookups, combine the bundled `AGENTS.md` with the GroupDocs MCP server at `https://docs.groupdocs.com/mcp`. See the [AI agents and LLM integration](https://docs.groupdocs.com/watermark/python-net/agents-and-llm-integration/) page for the per-tool setup snippets.

## Continuous integration

The `.github/workflows/` directory contains the CI matrix that runs the full example suite on every push. The matrix is reproducible locally via the `Dockerfile` above.

## More Resources

Find additional details and examples in the [GroupDocs.Watermark for Python via .NET documentation](https://docs.groupdocs.com/watermark/python-net/).

We also offer **GroupDocs.Watermark** packages for other platforms:
* [**GroupDocs.Watermark for .NET**](https://products.groupdocs.com/watermark/net/)
* [**GroupDocs.Watermark for Java**](https://products.groupdocs.com/watermark/java/)
* [**GroupDocs.Watermark for Node.js via Java**](https://products.groupdocs.com/watermark/nodejs-java/)

---

[Product Page](https://products.groupdocs.com/watermark/python-net/) | [Docs](https://docs.groupdocs.com/watermark/python-net/) | [Demos](https://products.groupdocs.app/watermark/family) | [API Reference](https://reference.groupdocs.com/watermark/python-net/) | [Blog](https://blog.groupdocs.com/category/watermark/) | [Search](https://search.groupdocs.com/) | [Free Support](https://forum.groupdocs.com/c/watermark) | [Temporary License](https://purchase.groupdocs.com/temporary-license)
