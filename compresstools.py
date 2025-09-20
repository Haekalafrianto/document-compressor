import os
import pikepdf
from PIL import Image

# --- PDF Compressor --- #
def compress_pdf(input_file, output_file):
    pdf = pikepdf.open(input_file)
    pdf.save(output_file, optimize=True, compress_streams=True, object_stream_mode=True)
    pdf.close()

    print(f"PDF compressed and saved to {output_file}")

# --- Image Compressor --- #
def compress_image(input_file, output_file, quality=60):
    img = Image.open(input_file)

    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    img.save(output_file, "JPEG", optimize=True, quality=quality)
    print(f"Image compressed and saved to {output_file}")

# --- Dispatcher --- #
def compress_file(input_file, output_file, file_type, quality=60):
    ext = os.path.splitext(input_file)[1].lower()

    if ext == "pdf" or ext == ".pdf":
        compress_pdf(input_file, output_file)
    elif ext in [".jpg", ".jpeg", ".png"]:
        compress_image(input_file, output_file)
    else:
        raise ValueError("Unsupported file type")