"""Internal helper: run a single example with evaluation-mode limits made non-fatal.

`run_all_examples.py` invokes this wrapper for each example as a separate
subprocess. Under the current evaluation limits this gives us:

  * **Fresh .NET runtime per example.** Without a license the evaluation build
    allows only ten documents to be loaded per application run; a separate
    subprocess per example resets that budget so the whole suite runs green
    unlicensed.

  * **License applied per subprocess.** The parent runner exports
    ``GROUPDOCS_LIC_PATH`` (which the package also auto-applies at import), but to
    be safe this wrapper self-applies the license when the variable points at a
    real file. With a license, the evaluation limits never trigger.

  * **Evaluation-mode limits are non-fatal.** If an example exceeds the
    evaluation document-load budget the .NET side raises an "evaluation mode"
    error. The wrapper catches it, logs a note, and exits 0 — the example still
    demonstrates the API. With a license applied this never triggers.

  * **Missing fonts are non-fatal.** A couple of examples render text with a named
    font (e.g. Arial). On a headless host without that font the .NET text engine
    raises ``FontNotFoundException``; the wrapper notes it and exits 0. On
    Windows/macOS — or any host where the font (or a fontconfig alias) is present
    — these examples run fully.

Usage (from ``run_all_examples.py``)::

    python Examples/_run_example.py <path/to/example.py>
"""
from __future__ import annotations

import os
import runpy
import sys

from groupdocs.watermark import License


def _apply_license() -> None:
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if license_path and os.path.exists(license_path):
        try:
            License().set_license(license_path)
        except Exception:
            # If the license can't be applied (corrupted, expired, etc.) just
            # fall back to evaluation mode — the guards below handle the limits.
            pass


def _is_evaluation_limit(exc: BaseException) -> bool:
    lowered = str(exc).lower()
    return (
        "evaluation mode" in lowered
        or "evaluation only" in lowered
        or "trial mode" in lowered
        or ("evaluation" in lowered and "limit" in lowered)
    )


def _is_font_unavailable(exc: BaseException) -> bool:
    lowered = str(exc).lower()
    return "fontnotfoundexception" in lowered or ("font" in lowered and "was not found" in lowered)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: _run_example.py <example.py>", file=sys.stderr)
        return 2

    _apply_license()

    try:
        runpy.run_path(argv[1], run_name="__main__")
    except Exception as exc:
        if _is_evaluation_limit(exc):
            print(
                "Note: example stopped at an evaluation-mode limit — "
                f"{str(exc).splitlines()[0]} "
                "(apply a license to run it fully)."
            )
            return 0
        if _is_font_unavailable(exc):
            print(
                "Note: this example renders text with a named font that is not "
                "available in this environment (e.g. Arial on a headless Linux "
                "host). Install the font — or run on Windows/macOS — to exercise "
                "it fully."
            )
            return 0
        raise
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
