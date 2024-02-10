from rembg import remove
from PIL import Image

image_input = Image.open("C:/Users/User/Desktop/Python Tricks")
output = remove("C:/Users/User/Desktop/Python Tricks/pic.png")
output.save("C:/Users/User")