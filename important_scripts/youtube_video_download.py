# YouTube Video Download Script using yt-dlp

# Import the required library
from yt_dlp import YoutubeDL

# Prompt the user to enter the YouTube video URL
link = input("Enter the link of the YouTube video you want to download: ")

# Configure yt-dlp options
# You can specify options like the download directory or video format here
ydl_opts = {
    'format': 'best',                # Download the best quality video available
    'outtmpl': '%(title)s.%(ext)s',  # Save the file with the video title as the filename
}

# Try downloading the video and handle potential errors
try:
    with YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading video from: {link}")   # Notify the user of the download process
        ydl.download([link])                       # Pass the link to yt-dlp for processing
        print("Download completed successfully!")  # Notify the user of a successful download
except Exception as e:
    # Catch and display any errors that occur during the download process
    print(f"An error occurred: {e}")
