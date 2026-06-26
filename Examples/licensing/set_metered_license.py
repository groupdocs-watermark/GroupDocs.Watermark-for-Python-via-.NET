from groupdocs.watermark import Metered

def set_metered_license():
    # Replace these placeholders with your real metered public/private keys
    public_key = "*****"
    private_key = "*****"

    # Skip the call until real keys are supplied (placeholder keys are rejected)
    if "*" in public_key or "*" in private_key:
        print("Provide real metered keys to enable metered licensing.")
        return

    # Apply the metered keys before using any watermarking features
    Metered().set_metered_key(public_key, private_key)
    print("Metered license set successfully.")

if __name__ == "__main__":
    set_metered_license()