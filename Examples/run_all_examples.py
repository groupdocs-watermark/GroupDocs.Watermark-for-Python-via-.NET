import os
import subprocess
import sys

# Use UTF-8 for stdout on Windows to avoid encoding errors when printing
# output that contains special Unicode characters
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Runner files that live alongside the examples but are not examples themselves.
RUNNER_FILES = {"run_all_examples.py", "_run_example.py"}

# Run the high-level sections in a natural order; everything else follows.
SECTION_ORDER = {"licensing": 0, "getting-started": 1, "developer-guide": 2}


def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Watermark for Python via .NET Examples!
=================================================================

This script runs a series of examples showcasing how to add, search, and remove
watermarks across PDF, Word, Excel, PowerPoint, Visio, image, and email formats
with GroupDocs.Watermark. Each example demonstrates a different use case, such as:

- Adding text, image, custom-font, and tiled watermarks.
- Adding PDF annotation/artifact watermarks and page-specific watermarks.
- Adding watermarks to presentation slides, Visio pages, images, and worksheets.
- Adding locked Word watermarks and spreadsheet background/header-footer watermarks.
- Searching watermarks by text, regex, image, formatting, and combined criteria.
- Modifying and removing found watermarks and hyperlinks.
- Working with existing document content, email messages, and attachments.
- Reading document info and listing supported formats.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API!

=======================================================
"""
    print(intro_text)


def announce_license():
    """Report whether GROUPDOCS_LIC_PATH points at a usable license file."""
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if license_path and os.path.exists(license_path):
        print(f"{GREEN}License available at: {license_path}{RESET}\n")
    else:
        print(f"{YELLOW}No license file found. Running in evaluation mode.{RESET}\n")


def discover_examples(base_dir):
    """Find every example script under base_dir, in a stable, readable order.

    Examples are any ``*.py`` file other than the runner helpers. Discovering them
    means new pages added to the docs are picked up automatically — no hand-kept list.
    """
    found = []
    for root, _, files in os.walk(base_dir):
        for name in sorted(files):
            if name.endswith(".py") and name not in RUNNER_FILES:
                rel = os.path.relpath(os.path.join(root, name), base_dir).replace(os.sep, "/")
                found.append(rel)

    def order_key(rel):
        return (SECTION_ORDER.get(rel.split("/", 1)[0], 99), rel)

    return sorted(found, key=order_key)


def run_example(base_dir, example_path):
    """Run a single example as a subprocess via the _run_example.py wrapper.

    Each example uses paths relative to its own folder, so the working directory
    is set to the example's directory. A fresh subprocess per example resets the
    evaluation build's ten-documents-per-application budget, and the wrapper
    applies the license (when GROUPDOCS_LIC_PATH is set) and makes evaluation-mode
    limits and missing-font errors non-fatal so the suite stays green unlicensed.
    """
    full_path = os.path.join(base_dir, example_path)
    example_dir = os.path.dirname(full_path)
    wrapper = os.path.join(base_dir, "_run_example.py")

    result = subprocess.run(
        [sys.executable, wrapper, full_path],
        cwd=example_dir,
        env=os.environ.copy(),
    )
    if result.returncode != 0:
        raise RuntimeError(f"subprocess exited with code {result.returncode}")


print_intro()
announce_license()

base_dir = os.path.dirname(os.path.abspath(__file__))
examples = discover_examples(base_dir)
print(f"Discovered {len(examples)} example(s).\n")

passed = 0
failed = 0

for example in examples:
    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        run_example(base_dir, example)
        print(f"{GREEN}Completed {example}{RESET}\n")
        passed += 1
    except Exception as e:
        print(f"{RED}Error in {example}: {type(e).__name__}: {e}{RESET}\n")
        failed += 1

print(f"\n{GREEN}Passed: {passed}{RESET}  {RED}Failed: {failed}{RESET}  Total: {passed + failed}")

sys.exit(1 if failed else 0)
