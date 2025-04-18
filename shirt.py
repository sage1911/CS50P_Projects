import sys
import os
from PIL import Image, ImageOps


if len(sys.argv) != 3:
    print("Usage: python lines.py <filename>")
    sys.exit(1)

input_image, output_image = sys.argv[1], sys.argv[2]    

input_ext = os.path.splitext(input_image)[1].lower()
output_ext = os.path.splitext(output_image)[1].lower()

valid_extensions = {".png", ".jpg", ".jpeg"}

if input_ext not in valid_extensions or output_ext not in valid_extensions:
    print("Error: Invalid file extension. Please use .jpg, .jpeg, or .png.")
    sys.exit(1)

if input_ext != output_ext:
    print("Error: Input and output file extensions must be the same.")
    sys.exit(1)

# Check if input file exists
if not os.path.exists(input_image):
    print("Error: Input file does not exist.")
    sys.exit(1)    


try:

    photo = Image.open(input_image)
    overlay = Image.open("shirt.png")

    resized_photo = ImageOps.fit((photo, overlay.size))

    resized_photo.paste(overlay, overlay)

    resized_photo.save(output_image)



except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
 
