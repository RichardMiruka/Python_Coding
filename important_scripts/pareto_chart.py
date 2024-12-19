# Pareto chart using Python

import pandas as pd
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Frequency': [10, 8, 6, 4, 2]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Sort the DataFrame by 'Frequency' in descending order
df = df.sort_values('Frequency', ascending=False)

# Calculate cumulative frequency and percentage
df['Cumulative Frequency'] = df['Frequency'].cumsum()
df['Cumulative Percentage'] = df['Cumulative Frequency'] / df['Frequency'].sum() * 100

# Plot the Pareto chart
fig, ax1 = plt.subplots()

# Bar chart for frequencies
ax1.bar(df['Category'], df['Frequency'], color="C4")
ax1.set_ylabel('Frequency')
ax1.set_xlabel('Category')

# Line chart for cumulative percentage
ax2 = ax1.twinx()
ax2.plot(df['Category'], df['Cumulative Percentage'], color="C1", marker="D", ms=7)
ax2.set_ylabel('Cumulative Percentage')

# Add a title
plt.title('Pareto Chart in Python')

# Show the plot
plt.show()
