"""
This script:
- Prompts the user to enter a place name.
- Uses the Nominatim service to fetch location details.
- Creates a map centered at the location, adds a marker,
 and saves the map as an HTML file.
- Handles errors and exceptions gracefully.
- Notifies the user about the successful creation of the map
and provides instructions to view it.
"""

import folium
from geopy.geocoders import Nominatim


def create_map_from_place(place_name):
    """
    Creates a map with a marker for the given place.

    Args:
        place_name (str): The name of the place to locate and map.

    Returns:
        None
    """
    # Initialize the geolocator
    geolocator = Nominatim(user_agent="geoapi")

    try:
        # Fetch the location details
        location = geolocator.geocode(place_name)

        if location:
            # Display location details
            print(f"Location found: {location.address}")
            print(f"Coordinates: {location.latitude}, {location.longitude}")

            # Create the map
            my_map = folium.Map(
                location=[location.latitude, location.longitude], zoom_start=12
            )

            # Add a marker
            folium.Marker(
                location=[location.latitude, location.longitude],
                popup=location.address,
                tooltip="Click for more info",
            ).add_to(my_map)

            # Save the map
            output_file = "mymap.html"
            my_map.save(output_file)
            print(
                f"Map created successfully! Open '{output_file}' in a browser to view it."
            )
        else:
            print(f"Could not find location: {place_name}. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Prompt the user for input
    place_name_input = input(
        "Enter the name of a place (e.g., San Francisco, Eiffel Tower): "
    )
    create_map_from_place(place_name_input)

    # Thank the user
    print("Thank you for using the map creator!")
    input("Press Enter to exit.")
    exit()
