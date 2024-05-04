import os

from PIL import Image
import numpy as np
import rawpy

input_folder = "./input_photos"
output_folder = "./output_photos"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".ARW"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        
        with rawpy.imread(input_path) as handler:
            rgb_img = handler.postprocess(use_camera_wb=True, half_size=False, no_auto_bright=True, output_bps=16)
            rgb_img = np.clip(rgb_img, 0, 65535).astype(np.uint16)
            rgb_img = np.float32(rgb_img) / 65535.0 
            rgb_img = (rgb_img * 255).astype(np.uint8)
            im = Image.fromarray(rgb_img)
            im.save(output_path)

print("All images processed and saved successfully.")
