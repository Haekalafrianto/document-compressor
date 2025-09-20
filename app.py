import os
from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
from compresstools import compress_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/compress', methods=['POST'])
def compress():
    file = request.files.get('file')
    input_file = file.filename
    output_file = "Compressed_" + input_file

    file.save(input_file)

    if input_file.lower().endswith(('.png', '.jpg', '.jpeg')):
        file_type = 'Image'
    elif input_file.lower().endswith('.pdf'):
        file_type = 'pdf'
    else:
        return "Unsupported file type", 400

    compress_file(input_file, output_file, file_type)

    return f"File compressed successfully, {output_file}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

