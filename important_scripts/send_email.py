# Send email using Python - smtplib

# pip install smtplib - Import the smtplib library

import smtplib

# Define the email details
my_email = "richard.miruka.dev@gmail.com"  # Your email address
password = "dhed meic wwej rqzf"  # Your email password

# Create the email server
connection = smtplib.SMTP("smtp.gmail.com", 587)  # Connect to the Gmail server on port 587 (TLS encryption)
connection.starttls()  # Use TLS encryption to secure the connection
connection.login(user = my_email, password = password)  # Login to your email account

# Send the email
connection.sendmail(from_addr = my_email, to_addrs = "richardmiruka96@gmail.com", msg = "Subject:Hello\n\nThis is a test email.")  # Send the email with the subject "Hello" and the message "This is a test email."
connection.close()  # Close the connection to the email server after sending the email 
