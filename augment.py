# augment.py
import sys
import os
from PIL import Image, ImageEnhance
import random

def augment_image(image_path, output_folder):
    img = Image.open(image_path)
    basename = os.path.basename(image_path)
    name, ext = os.path.splitext(basename)

    # Apply random transformations
    img = img.rotate(random.randint(-10, 10))
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(random.uniform(0.7, 1.3))
    img.save(os.path.join(output_folder, f"{name}_aug{ext}"))

if __name__ == "__main__":
    input_image = sys.argv[1]
    output_folder = sys.argv[2]
    os.makedirs(output_folder, exist_ok=True)
    augment_image(input_image, output_folder)
