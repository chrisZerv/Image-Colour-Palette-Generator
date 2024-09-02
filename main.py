from flask import Flask, request, render_template, redirect, url_for
import cv2
import numpy as np
from PIL import Image
from collections import Counter
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions for image files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            colors = get_colors(file_path)
            return render_template('results.html', colors=colors)
    elif 'redirect' in request.args:
        return redirect(url_for('upload_file'))
    return render_template('index.html')


def get_colors(image_path):
    # Load image and convert it to RGB
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)

    # Convert pixels to tuples and count the occurrences
    pixel_counts = Counter([tuple(pixel) for pixel in pixels])

    # Get the total number of pixels
    total_pixels = len(pixels)

    # Get the most common colors
    most_common_colors = pixel_counts.most_common(10)

    # Convert colors from RGB to HEX and calculate percentages
    colors_with_percentage = [
        {'color': '#{:02x}{:02x}{:02x}'.format(*color[0]),
         'percentage': round((color[1] / total_pixels) * 100, 2)}
        for color in most_common_colors
    ]

    return colors_with_percentage


if __name__ == '__main__':
    app.run(debug=True)
