# Run the script and provide the path to a PDF file when prompted. 
#The script will convert the PDF to a Word document and save it at the specified location.
# A success message will be displayed upon completion.

# pip insatll pdf2docx

from pdf2docx import Converter                                             # Import the Converter class from the pdf2docx library

pdf_file = input("Enter the path to the PDF file: ")                       # Prompt the user to enter the path to the PDF file
docx_file = input("Enter the path to save the converted Word document: ")  # Prompt the user to enter the path to save the converted Word document

converter = Converter(pdf_file)                          # Create an instance of the Converter class with the PDF file path
converter.convert(docx_file)                             # Convert the PDF file to a Word document and save it at the specified path
converter.close()                                        # Close the Converter instance

print("PDF converted to Word successfully.")             # Print a message to indicate successful conversion
