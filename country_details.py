# The countryinfo package provides a convenient way to retrieve detailed information about countries using Python.
# The package allows you to access a wide range of information about countries, including their names, capitals,
# populations, currencies, languages, regions, flags, timezones, and more.
# To use the countryinfo package, you need to install it using pip:
# pip install countryinfo

from countryinfo import CountryInfo                    # Import the CountryInfo class from the countryinfo package

country_name = input("Enter the country name: ")       # Prompt the user for the country name
country = CountryInfo(country_name)                    # Create a CountryInfo object with the given country name

try:
    country_info = country.info()                                        # Get all information about the country in a dictionary format
    print("Country Details:")
    print(f"Name: {country_info.get('name', 'N/A')}")                         # Get the country's name, defaulting to 'N/A' if not found
    print(f"Capital: {country_info.get('capital', 'N/A')}")                   # Get the capital, with a default if unavailable
    print(f"Population: {country_info.get('population', 'N/A')}")             # Get the population
    print(f"Currency: {country_info.get('currencies', 'N/A')}")               # Get the currency (note: it may be a list)
    print(f"Language(s): {country_info.get('languages', 'N/A')}")             # Get languages spoken in the country
    print(f"Area: {country_info.get('area', 'N/A')} sq. km")                  # Get the area in square kilometers
    print(f"Region: {country_info.get('region', 'N/A')}")                     # Get the region where the country is located
    print(f"Subregion: {country_info.get('subregion', 'N/A')}")               # Get the subregion where the country is located
    print(f"Flag: {country_info.get('flags', {}).get('png', 'N/A')}")         # Get the URL to the country's flag image
    print(f"Wiki Page: {country_info.get('wikipedia', 'N/A')}")               # Get the Wikipedia page URL for the country
    print(f"Timezones: {country_info.get('timezones', 'N/A')}")               # Get the timezones for the country
    print(f"Neighbours: {country_info.get('borders', 'N/A')}")                # Get the neighbouring countries
    print(f"Calling Code: {country_info.get('callingCodes', 'N/A')}")         # Get the calling code(s) for the country
    print(f"Latitude/Longitude: {country_info.get('latlng', 'N/A')}")         # Get the latitude and longitude of the country 
except KeyError:
    print("Country details not found. Please check the country name and try again.") # Handle the case where country details are not found
