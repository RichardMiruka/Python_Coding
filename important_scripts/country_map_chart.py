#!/usr/bin/env python

# Importing the required library for creating interactive visualizations
# Ensure you have Plotly installed: pip install plotly
import plotly.express as px

# Defining the dataset as a dictionary
# The data contains a list of countries and their corresponding values
data = {
    # List of countries
    "Country": ["USA", "Canada", "UK", "Germany", "France"],
    # Corresponding values for each country
    "Values": [100, 200, 150, 75, 300],
}

# Creating a choropleth map using Plotly Express
# A choropleth map visualizes data through varying shades of color on a map
fig = px.choropleth(
    data_frame=data,  # Input data
    locations="Country",  # Column in data specifying the country names
    locationmode="country names",  # Match the country names to the map
    color="Values",  # Column in data that determines the color intensity
    color_continuous_scale="viridis",  # Color scale for the data values
    projection="natural earth",  # Type of map projection
    title="Country Values",  # Title of the map
)

# Displaying the generated choropleth map
fig.show()
