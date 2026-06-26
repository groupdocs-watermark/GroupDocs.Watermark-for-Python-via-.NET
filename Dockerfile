FROM python:3.13-slim

# System dependencies for the .NET runtime: libicu-dev (globalization)
# and libgdiplus + libfontconfig1 (System.Drawing / GDI+, used by the
# image and rasterized rendering paths on Linux)
RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends libicu-dev libgdiplus libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install the package from PyPI. The image is Linux/x86_64, so pip selects the
# manylinux1_x86_64 wheel automatically.
COPY Examples/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy examples and sample files
COPY Examples/ ./Examples/

# Run all examples
CMD ["python", "Examples/run_all_examples.py"]
