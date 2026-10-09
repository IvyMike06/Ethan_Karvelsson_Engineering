from PIL import Image
from pathlib import Path

# Folder containing your original images
input_folder = Path("images")

# Folder where compressed images will be saved
output_folder = Path("images-optimized")

# Create the output folder if it doesn't exist
output_folder.mkdir(exist_ok=True)

# Maximum dimension for the longest side of an image
max_size = 2400

# JPEG quality
quality = 85


# Go through every file in the images folder
for file in input_folder.iterdir():

    # Only process common image files
    if file.suffix.lower() not in [".jpg", ".jpeg", ".png", ".webp"]:
        continue

    try:
        # Open the image
        image = Image.open(file)

        # Resize if the image is larger than max_size
        image.thumbnail((max_size, max_size))

        # Create output filename
        output_file = output_folder / (file.stem + ".jpg")

        # Convert to RGB and save as JPEG
        image.convert("RGB").save(
            output_file,
            "JPEG",
            quality=quality,
            optimize=True
        )

        print(f"Compressed: {file.name}")

    except Exception as e:
        print(f"Could not process {file.name}: {e}")

print("\nDone!")