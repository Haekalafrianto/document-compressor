import os
from flask import Flask, request, send_file, render_template_string
from werkzeug.utils import secure_filename
from compresstools import compress_file

try:
    compress_file("sample.pdf", "sample_compressed.pdf")
    compress_file("sample.png", "sample_compressed.jpg")
except Exception as e:
    print(e)