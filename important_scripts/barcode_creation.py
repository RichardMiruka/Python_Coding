# Barcode creation using Python

# pip install python-barcode - Import the required modules from the python-barcode library

import barcode
from barcode.writer import ImageWriter         # Import the ImageWriter class from the writer module
from IPython.display import Image, display     # Import the Image class from the IPython.display module

barcode_format = barcode.get_barcode_class('code128')  # Specify the barcode format (code128 in this case)

barcode_number = '1234567895540'              # Define the barcode number to be generated
barcode_image = barcode_format(barcode_number, writer=ImageWriter())  # Generate the barcode image

# Save the barcode image to a file
barcode_filename = "barcode_image"                 # Define the filename for the barcode image
barcode_image.save(barcode_filename)               # Save the barcode image with the specified filename

# Display the generated barcode image
display(Image(filename=f"{barcode_filename}.png"))  # Display the barcode image using IPython.display
