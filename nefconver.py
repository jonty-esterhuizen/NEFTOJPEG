import rawpy
from PIL import Image
import os

def convert_nef_to_jpeg():
    current_directory = os.getcwd()
    output_directory = os.path.join(current_directory, "converted_jpegs")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(current_directory):
        if filename.lower().endswith(".nef"):
            try:
                # Open the NEF file using rawpy to preserve quality and resolution
                raw = rawpy.imread(os.path.join(current_directory, filename))
                rgb_image = raw.postprocess()

                # Convert to a Pillow Image object
                img = Image.fromarray(rgb_image)

                # Save the image as JPEG with high quality and original resolution
                base_filename = os.path.splitext(filename)[0]
                output_path = os.path.join(output_directory, f"{base_filename}.jpeg")
                img.save(output_path, "JPEG", quality=95)
                print(f"Converted {filename} to {output_path} with high quality and original resolution")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    convert_nef_to_jpeg()
