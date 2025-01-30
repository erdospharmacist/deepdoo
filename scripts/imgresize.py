from PIL import Image
import os

folder_path = os.path.expanduser("/Users/ethanteicher/Desktop/Programming/realdpimages") 

new_size = (512, 512)  

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
        with Image.open(file_path) as img:
            # Resize while maintaining quality
            img_resized = img.resize(new_size, Image.LANCZOS)
            
            # Save back to the same location, overwriting
            img_resized.save(file_path)
print("Resizing complete.")
