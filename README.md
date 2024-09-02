# Color Extractor Web Application

This is a simple web application built with Python and Flask that allows users to upload an image and find the top 10 most common colors in the image, along with the percentage that each color represents. The application uses OpenCV for image processing.

## Features

- Upload an image and extract the top 10 most common colors.
- Display the HEX code and percentage of each color.
- Responsive UI built with Bootstrap.
- Simple and clean design with the ability to change themes using Bootswatch.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/color-extractor.git
    cd color-extractor
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open your web browser and go to `http://localhost:5000/` to access the application.

## Usage

1. Visit the application in your browser.
2. Upload an image by clicking on the "Choose File" button and selecting an image file from your computer.
3. Click the "Upload" button to process the image.
4. The application will display the top 10 most common colors in the image, along with their HEX codes and the percentage they represent.
5. To analyze another image, click the "Upload another image" button.


## File Structure

```plaintext
color-extractor/
│
├── app.py               # Main Flask application
├── uploads/             # Directory to store uploaded images
├── templates/           # HTML templates
│   ├── index.html       # Upload form
│   └── results.html     # Results display
├── requirements.txt     # Python dependencies
└── README.md            # This README file

