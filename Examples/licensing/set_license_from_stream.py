import os
from groupdocs.watermark import License

def set_license_from_stream():
    # Resolve the license path from the environment, with a local fallback
    license_path = os.environ.get("GROUPDOCS_LIC_PATH", "./GroupDocs.Watermark.lic")

    # Apply the license from an open binary stream
    if os.path.exists(license_path):
        with open(license_path, "rb") as stream:
            License().set_license(stream)
        print("License set successfully.")
    else:
        print("License file not found. Running in evaluation mode.")

if __name__ == "__main__":
    set_license_from_stream()