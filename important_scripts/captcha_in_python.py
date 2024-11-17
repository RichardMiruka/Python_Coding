# CAPTCHA in Python using captcha library

# pip install captcha

from captcha.image import ImageCaptcha                 # Import ImageCaptcha for generating CAPTCHA images
from PIL import Image                                  # Import PIL for image handling
import random                                          # Import random module for generating random strings
import string                                          # Import string module for character sets

# Function to generate random CAPTCHA text
def generate_captcha_text(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) # Generate a string of random letters and digits of specified length

# Function to generate a CAPTCHA image from text
def generate_captcha_image(captcha_text, image_width=300):
    image = ImageCaptcha(image_width)                      # Create a CAPTCHA image with specified width
    image_file = f"{captcha_text}.png"                     # File name based on the CAPTCHA text
    image.write(captcha_text, image_file)                  # Write the CAPTCHA text onto the image
    return image_file                                      # Return the name of the generated image file


captcha_text = generate_captcha_text()                     # Ge     nerate a random CAPTCHA text
image_file = generate_captcha_image(captcha_text)          # Create and save the CAPTCHA image

# Print confirmation and display the image
print(f"Generated CAPTCHA: {captcha_text}")                # Print the CAPTCHA text
Image.open(image_file).show()                              # Open the generated image for viewing
