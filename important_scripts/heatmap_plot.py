# creating a heatmap plot using python

import matplotlib.pyplot as plt   # importing matplotlib
import numpy as np                # importing numpy
import seaborn as sns             # importing seaborn

data = np.random.rand(10, 12)     # generating random data for the heatmap plot (10x12 matrix) using numpy random function (values between 0 and 1)
sns.heatmap(data, cmap='plasma')  # creating a heatmap plot using seaborn with the 'plasma' colormap (color map) and the random data generated above
plt.show()                        # displaying the heatmap plot using matplotlib plt.show() function 
