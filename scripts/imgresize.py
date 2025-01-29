import os
from PIL import Image

def resize_image(input_path, output_size=(512, 512)):
    try:
        img = Image.open(input_path)
        resized_img = img.resize(output_size)
        return resized_img
    except Exception as e:
        print(f"Error resizing {input_path}: {e}")
        return None

def main():
    #this is what i have my folder called, insert your own.
    input_folder = "realdpimages"
    output_folder = input_folder  # Resize in place
    
    if not os.path.exists(input_folder):
        print(f"Folder '{input_folder}' does not exist.")
        return
    
    # Get all files in the folder
    file_list = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    count = 0
    for filename in file_list:
        # Full path to the file
        input_path = os.path.join(input_folder, filename)
        
        # Resizing the image
        resized_image = resize_image(input_path)
        
        if resized_image is not None:
            # Create new filename with the desired format
            new_name = f"real_image_{count + 1}.png"
            output_path = os.path.join(output_folder, new_name)
            
            try:
                # Save the resized image
                resized_image.save(output_path, "PNG")
                
                # Optional: Delete original file if you want to replace it
                os.remove(input_path)
                print(f"Resized and renamed: {filename} -> {new_name}")
            except Exception as e:
                print(f"Error saving/resizing {filename}: {e}")
        
        count += 1

if __name__ == "__main__":
    main()
