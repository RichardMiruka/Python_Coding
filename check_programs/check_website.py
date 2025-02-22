import requests

def check_website(url):
    """
    Sends a GET request to the given URL with a short timeout.
    Returns True if the website responds with a status code less than 400,
    otherwise returns False.
    """
    try:
        # Using GET here; you could also try requests.head() for a lightweight check.
        response = requests.get(url, timeout=5)
        return response.status_code < 400
    except requests.RequestException:
        return False

def main():
    # Read each line from the addresses.txt file.
    # It assumes each address is on a separate line.
    with open("addresses.txt", "r") as file:
        addresses = [line.strip() for line in file if line.strip()]

    for address in addresses:
        # If the address doesn't start with http:// or https://, prepend http://
        if not (address.startswith("http://") or address.startswith("https://")):
            url = "http://" + address
        else:
            url = address
        
        # Check if the website is up
        if check_website(url):
            status = "up"
        else:
            status = "down"
        
        # Output the original address along with its status.
        print(f"{address} {status}")

if __name__ == '__main__':
    main()
