# This script creates a map using the Folium library in Python. It sets
# the center of the map to San Francisco, adds a marker at that location,
# and then saves the map to an HTML file. The user is notified about the
# successful creation of the map and instructed to open the HTML file in a
# browser to view it.

# Create a map using Python
# pip install folium

import folium
from Ipython.display import display

# Create a map centered at a specific location
map_center = [37.7749, -122.4194]  # San Francisco coordinates
mymap = folium.Map(location=map_center, zoom_start=12)

# Add a marker to the map
marker = folium.Marker(location=[37.7749, -122.4194], popup="San Francisco")
marker.add_to(mymap)

# Save the map to an HTML file
mymap.save("mymap.html")

# Notify the user
print("Map created successfully! Open 'mymap.html' in a browser to view it.")
