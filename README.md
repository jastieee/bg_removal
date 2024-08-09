# bg_removal

# Background Removal Project

This project is designed to automate the process of removing and replacing the background of images. The tool uses Python libraries such as `os`, `tkinter`, and `OpenCV` to provide a user-friendly interface for selecting images and backgrounds, and for saving the processed images.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## About the Project

The Background Removal Project allows users to:
1. **Browse and select images** from a directory using a graphical interface.
2. **Remove the background** from the selected images.
3. **Choose a new background** for the images.
4. **Save the processed images** with appropriate naming conventions in a specified folder.
5. **Repeat the process** as needed by reselecting images and backgrounds.

## Features

- **Folder Browsing**: The tool uses the `os` module to list folders for original images, masked images, and background images.
- **Graphical Interface**: Tkinter is used to open the root directory, allowing users to freely choose which image to process.
- **Background Removal and Replacement**: After selecting an image, the background can be removed and replaced with a new one.
- **Automated Saving**: The processed images are saved in a "masked" folder, with names like `masked_filename.jpg` for background removal and `background_number.jpg` for images with a replaced background.
- **Easy Re-selection**: A window opens using OpenCV, allowing users to press 'n' to pick a new image and background.

## Technologies Used

- **Python**: Core language used for scripting.
- **OS Module**: Used for directory and file operations.
- **Tkinter**: Provides the graphical user interface for file selection.
- **OpenCV**: Handles image processing and displays the result.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone[https://github.com/jastieee/bg_removal.git]
    cd background-removal-project
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the project**:
    ```bash
    python main.py
    ```

## Usage

1. **Select the Original Image**: When prompted, choose an image from the original images folder.
2. **Select the Background Image**: After the background is removed, select a new background image.
3. **Save the Processed Image**: The processed image will be automatically saved in the masked folder with the correct naming conventions.
4. **Repeat**: Press 'n' in the OpenCV window to process another image.

## Contact

For any questions or feedback, feel free to reach out:

- **Name**: Jhustie Mae Cruz
- **Email**: cruzjastie@gmail.com
- **GitHub**: [jastieee](https://github.com/jastieee)
