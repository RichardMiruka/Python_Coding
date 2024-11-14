import qrcode

# Create an instance of the QRCode object
qr = qrcode.QRCode(
    version=1,                                          # QR code version (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level (L, M, Q, H)
    box_size=10,                                        # Size of each box in the QR code
    border=4,                                           # Size of the border around the QR code
)

# Add data to the QR code
qr.add_data("https://x.com/RichardOnsare1")             # Data to be encoded in the QR code
qr.make(fit=True)                                       # Generate the QR code

# Save the QR code as an image file
qr.make_image(fill_color="black", back_color="white").save("qr_code.png")  # Specify colors and save the QR code as a PNG file
print("QR code generated and saved as 'qr_code.png'")                      # Print a message to indicate successful generation
