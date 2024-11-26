# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup


def get_weather(city_name):
    """
    Fetch and display weather information for the given city.

    Args:
        city_name (str): The name of the city to fetch weather for.

    Returns:
        None
    """
    # Format the city name for use in the URL
    city_formatted = city_name.lower().replace(" ", "+")
    url = f"https://www.google.com/search?q=weather+in+{city_formatted}"

    try:
        # Send a GET request to the weather information URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract weather details from the page
        temperature = soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
        weather = soup.find("div", class_="BNeawe tAd8D AP7Wnd").text

        # Display the weather information
        print(f"The weather in {city_name} is {temperature} and {weather}.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching weather data: {e}")
    except AttributeError:
        print("Weather information not found. Please try again.")


if __name__ == "__main__":
    # Get the city name from the user
    city = input("Enter the city name: ")
    get_weather(city)
