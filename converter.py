import os
import shutil
from docx2pdf import convert

# Folder structure
INPUT_DIR = "input"
OUTPUT_DIR = "outputPdfs"
CONVERTED_DIR = "convertedDocs"

def ensure_folders():
    """Create folders if they don't exist."""
    for folder in [INPUT_DIR, OUTPUT_DIR, CONVERTED_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)

def convert_docx_to_pdf():
    ensure_folders()

    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".docx")]

    if not files:
        print("⚠️ No .docx files found in 'input' folder.")
        return

    success_count = 0
    fail_count = 0

    for file in files:
        input_path = os.path.join(INPUT_DIR, file)
        output_path = os.path.join(OUTPUT_DIR, file.replace(".docx", ".pdf"))
        converted_path = os.path.join(CONVERTED_DIR, file)

        try:
            convert(input_path, output_path)
            print(f"✅ Converted: {file} → {output_path}")

            # Move original docx to convertedDocs
            shutil.move(input_path, converted_path)
            print(f"📦 Moved original: {file} → {converted_path}")

            success_count += 1

        except Exception as e:
            print(f"❌ Failed to convert {file}: {e}")
            fail_count += 1

    # Print summary
    print("\n--- Conversion Summary ---")
    print(f"📄 Total files processed: {len(files)}")
    print(f"✅ Successfully converted: {success_count}")
    print(f"❌ Failed conversions: {fail_count}")

if __name__ == "__main__":
    convert_docx_to_pdf()
