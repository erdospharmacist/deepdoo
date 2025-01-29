import torch
import accelerate
from diffusers import StableDiffusionPipeline
import os
import random

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the Stable Diffusion pipeline
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to(device)  # Use GPU if available

# Set directory for output
output_dir = "dpimages"
os.makedirs(output_dir, exist_ok=True)

# Function to generate and save images
def gen_img(prompts, num_images, output_dir):
    for i in range(num_images):
        prompt = random.choice(prompts)  # Choose a random prompt
        image = pipe(prompt).images[0]
        image_path = os.path.join(output_dir, f"image_{i+1}.png")
        image.save(image_path)
        print(f"Saved {image_path}")

prompts = [
    "hyperrealistic black or brown dog poo on synthetic turf",
    "out of focus hyperrealistic black or brown dog feces on fake green grass",
    "hyperrealistic brown dog feces on artificial grass field, in shade with rocks",
    "dog feces on plastic grass, next to rocks or rope, hyperrealistic, weird angles"
]

# Call the function to generate and save images
gen_img(prompts, num_images=100, output_dir=output_dir)
