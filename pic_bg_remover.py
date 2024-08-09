from rembg import remove
import os
from PIL import Image
import cv2
import tkinter as tk
from tkinter import filedialog
import random

# Define directories
original_dir = 'original'
masked_dir = 'masked'
background_dir = 'bg_image'

# Ensure directories exist
os.makedirs(original_dir, exist_ok=True)
os.makedirs(masked_dir, exist_ok=True)

def list_images(directory):
    """List all images in a directory and return the list of image filenames."""
    files = os.listdir(directory)
    images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    return images

def choose_image_file():
    """Open file dialog to select an image file."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        initialdir=original_dir,
        title="Select an image",
        filetypes=[("Image files", ".jpg;.jpeg;*.png")]
    )
    return file_path

def remove_background(img_path, output_path):
    """Remove background from the image and save it."""
    with open(output_path, 'wb') as f:
        input_img = open(img_path, 'rb').read()
        subject = remove(input_img)
        f.write(subject)

def choose_background():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        initialdir=background_dir,
        title="Select an image",
        filetypes=[("Image files", ".jpg;.jpeg;*.png;.jfif")]
    )
    return file_path

def update_background(background_img_path, masked_img_path):
    """Update the background image and save the composite."""

    background_img = Image.open(background_img_path)
    background_img = background_img.resize((1020, 720))

    foreground_img = Image.open(masked_img_path)
    
    background_img.paste(foreground_img, (0, 0), foreground_img)
    
    if background_img.mode != 'RGB':
        background_img = background_img.convert('RGB')

    def get_next_filename(base_path, extension):
        existing_files = os.listdir(os.path.dirname(base_path))
        indices = []
        for file in existing_files:
            if file.startswith(os.path.basename(base_path)) and file.endswith(extension):
                try:
                    index = int(file.split('_')[-1].split('.')[0])
                    indices.append(index)
                except ValueError:
                    continue
        next_index = max(indices, default=0) + 1
        return f'{base_path}_{next_index}{extension}'

    base_path = 'masked/background'
    extension = '.jpg'
    result_path = get_next_filename(base_path, extension)
    background_img.save(result_path, format='jpeg')

    # Open and display images
    masked_img_cv2 = cv2.imread(masked_img_path)
    result_img_cv2 = cv2.imread(result_path)

    masked_img_cv2 = cv2.resize(masked_img_cv2, (1020, 720))
    result_img_cv2 = cv2.resize(result_img_cv2, (1020, 720))

    cv2.namedWindow('Masked Image (Background Removed)', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Masked Image (Background Removed)', 1020, 720)
    cv2.imshow('Masked Image (Background Removed)', masked_img_cv2)

    cv2.namedWindow('Image with New Background', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image with New Background', 1020, 720)
    cv2.imshow('Image with New Background', result_img_cv2)

def change_background():
    """Change the background image from the list of available images."""
    listImg = os.listdir(background_dir)
    if not listImg:
        print("No background images found.")
        return

    # Open file dialog to select the image to process
    img_path = choose_image_file()
    if not img_path:
        print("No image selected.")
        return
    
    background_img_path = choose_background()
    if not background_img_path:
        print("No backgrouns selected.")
        return
    

    masked_img_path = os.path.join(masked_dir, f'masked_{os.path.basename(img_path)}')
    remove_background(img_path, masked_img_path)
    update_background(background_img_path, masked_img_path)

change_background()

while True:
    key = cv2.waitKey(0)  
    if key == ord('n'):  # 'n' key to change background
        change_background()
    elif key == ord('q'):  # 'q' key to quit
        break

cv2.destroyAllWindows()