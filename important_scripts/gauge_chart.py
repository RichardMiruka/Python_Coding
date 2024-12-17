import plotly.graph_objects as go

# Define the data for the gauge chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=75,
    title={"text": "Speed"},
    gauge={"axis": {"range": [0, 100]},
           "steps": [{"range": [0, 20], "color": "red"},
                     {"range": [20, 40], "color": "orange"},
                     {"range": [40, 60], "color": "yellow"},
                     {"range": [60, 80], "color": "lightgreen"},
                     {"range": [80, 100], "color": "green"}],
           "threshold": {"value": 50, "thickness": 0.75, "line": {"color": "red", "width": 4}}}
))

# Set the title of the chart
fig.update_layout(title_text="Gauge Chart in Python")
margin = dict(t=30, left=0, right=0, bottom=0)  # Set the margin for the chart

fig.show()  # Display the chart
