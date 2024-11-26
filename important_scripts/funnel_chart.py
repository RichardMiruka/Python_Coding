# The funnel chart is a type of chart that represents stages of a process
# or system as progressively decreasing proportions. Each stage is
# represented by a segment of the funnel, with the width of the segment
# corresponding to the value or size of that stage. Funnel charts are
# commonly used in marketing and sales to visualize the conversion rates
# or drop-off rates at each stage of a sales or marketing funnel.

import plotly.graph_objects as go

# Define the data for the funnel chart
stages = ["A", "B", "C", "D"]
values = [1000, 750, 500, 250]

# Create the funnel chart
fig = go.Figure(go.Funnel(
    y=stages,  # Define the stages of the funnel
    x=values,  # Define the values for each stage
    textinfo="value+percent total",  # Display the value and percentage
    marker=dict(
        color=[
            "deepskyblue",
            "lightsalmon",
            "tan",
            "teal"]),
    # Define the colors for each stage
))

# Set the title of the chart
fig.update_layout(title_text="Funnel Chart in Python")
margin = dict(t=30, left=0, right=0, bottom=0)  # Set the margin for the chart

fig.show()  # Display the chart
