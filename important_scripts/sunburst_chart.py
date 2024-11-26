# The sunburst chart is a hierarchical chart that represents
# the data in a circular format. Each segment of the chart represents
# a category or value, with the root segment at the center and branches
# and leaves extending outward. The size of each segment is proportional
# to the value it represents, allowing for easy visualization of the data
# hierarchy and distribution.

import plotly.graph_objects as go

# Define the data for the sunburst chart
labels = ["Root", "Branch 1", "Branch 2", "Leaf 1", "Leaf 2", "Leaf 3"]
parents = ["", "Root", "Root", "Branch 1", "Branch 1", "Branch 2"]
values = [10, 5, 5, 2, 3, 5]

# Create the sunburst chart
fig = go.Figure(
    go.Sunburst(
        labels=labels,  # Define the labels for each segment
        parents=parents,  # Define the parent segments
        values=values,  # Define the values for each segment
        branchvalues="total",  # Set the branch values to total
    )
)

# Set the title of the chart
fig.update_layout(title_text="Sunburst Chart in Python")
margin = dict(t=30, left=0, right=0, bottom=0)  # Set the margin for the chart

fig.show()  # Display the chart
