import os
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image

# --- PDF Compressor --- #
def compress_pdf(input_file, output_file):
    reader = PdfReader(input_file)
    writter = PdfWriter()

    for page in reader.pages:
        writter.add_page(page)

    writter.add_metadata(reader.metadata)

    with open(output_file, "wb") as f:
        writter.write(f)

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