import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

#scatter plot

x=[10,20,30]
y=[10,50,60]
plt.scatter(x,y,c="yellow",marker="o",s=105,alpha=0.5)
#plt.show()

#line plot
import matplotlib.pyplot as plt

years = [2005, 2006, 2007, 2008, 2009]
weight = [40, 50, 60, 70, 80]

plt.figure(figsize=(8, 5))  # Adjust figure size for better readability
plt.plot(years, weight, marker='o', linestyle='-', color='b', linewidth=2, markersize=8, label="Weight Trend")

plt.xlabel("Years")
plt.ylabel("Weight (kg)")
plt.title("Weight Progress Over the Years")

plt.xticks(years)  # Ensure all years are shown on x-axis
plt.yticks(range(min(weight), max(weight) + 10, 10))  # Adjust y-axis ticks for better readability

plt.grid(True, linestyle="--", alpha=0.6)  # Add grid lines for better visualization
plt
plt.show()
