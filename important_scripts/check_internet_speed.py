# Check internet speed using Python

# pip install speedtest-cli - Import the speedtest module from the speedtest-cli library
import speedtest

def check_internet_speed():                               # Define a function to check the internet speed
    test = speedtest.Speedtest()                         # Initialize a Speedtest object

    # Perform the download speed test and convert the result to Mbps
    download_speed = test.download()                     # Get the download speed in bits per second
    download_speed = round(download_speed / 10**6, 2)    # Convert from bits per second to megabits per second
    print(f"Download Speed: {download_speed} Mbps")      # Print the download speed

    # Perform the upload speed test and convert the result to Mbps
    upload_speed = test.upload()                         # Get the upload speed in bits per second
    upload_speed = round(upload_speed / 10**6, 2)        # Convert from bits per second to megabits per second
    print(f"Upload Speed: {upload_speed} Mbps")          # Print the upload speed

    # Get the ping (latency) result in milliseconds
    test.get_best_server()                               # Identify the best server for accurate ping measurement
    ping = test.results.ping                             # Get the ping value in milliseconds
    print(f"Ping: {ping} ms")                            # Print the ping value

# Call the function to check the internet speed
check_internet_speed()
