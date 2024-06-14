from rembg import remove
from PIL import Image

# Open the input image
image_input_path = "C:/Users/User/Desktop/Python Tricks/mountain.jpg"
image_output_path = "C:/Users/User/Desktop/Python Tricks/mountain_no_bg.png"

# Open the input image
image_input = Image.open(image_input_path)

# Remove the background
output = remove(image_input)

# Save the output image as PNG
output.save(image_output_path)
