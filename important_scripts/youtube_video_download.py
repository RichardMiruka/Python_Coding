# Youtube video download script

# pip install pytube

import pytube # Import the pytube library

link = input("Enter the link of the Youtube video you want to download: ")  # Prompt the user to enter the link of the video they want to download
yt = pytube.YouTube(link)  # Create a YouTube object with the video link provided by the user and store it in the 'video' variable 
yt.streams.first().download()  # Download the highest resolution video stream from the video object and save it in the current directory

print('downloaded', link)  # Display a success message after downloading the video successfully
