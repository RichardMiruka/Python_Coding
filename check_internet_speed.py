# check internet spped using python

# pip install speedtest-cli - Import the speedtest module from the speedtest-cli library

import speedtest as st

def check_internet_speed():                               # Define a function to check the internet speed
    test = st.Speedtest()                                 # Initialize a Speedtest object

    # Perform the download speed test and convert the result to Mbps
    download_speed = test.download()                      # Get the download speed in bytes
    download_speed = round(download_speed / 10**6, 2)     # Convert from bits per second to megabits per second
    print(f"Download Speed: {download_speed} Mbps")       # Print the download speed

    # Perform the upload speed test and convert the result to Mbps
    upload_speed = test.upload()
    upload_speed = round(upload_speed / 10**6, 2)          # Convert from bits per second to megabits per second
    print(f"Upload Speed: {upload_speed} Mbps")            # Print the upload speed

    # Get the ping (latency) result in milliseconds
    ping = test.results.ping
    print(f"Ping: {ping} ms")
check_internet_speed()                                      # Call the function to check the internet speed
