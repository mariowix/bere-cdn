from PIL import Image
import os

def trim_image(input_path, output_path):
    # Open the image
    image = Image.open(input_path)

    # Get the bounding box of the non-empty pixels
    bbox = image.getbbox()

    # Crop the image using the bounding box
    cropped_image = image.crop(bbox)

    # Save the cropped image
    cropped_image.save(output_path)

def trim_images_in_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".webp"):
            try:
                # Trim the image
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                trim_image(input_path, output_path)
                print(f"Trimmed {filename} successfully.")
            except Exception as e:
                print(f"Error trimming {filename}: {e}")

# Example usage
input_folder = "normal"
output_folder = "processed"
trim_images_in_folder(input_folder, output_folder)
