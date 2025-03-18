import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

#scatter plot

years = [2005, 2006, 2007, 2008, 2009]
weight = [40, 50, 60, 70, 80]
plt.scatter(years,weight,c="yellow",marker="o",s=105,alpha=0.5)
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
plt.yticks(range(min(weight), max(weight) + 10, 5))  # Adjust y-axis ticks for better readability

plt.grid(True, linestyle="--", alpha=0.6)  # Add grid lines for better visualization
plt
plt.show()

#bar plot
years = [2005, 2006, 2007, 2008, 2009]
weight = [40, 50, 60, 70, 80]

plt.barh(years,weight,align="center")
plt.show()
git add .
git commit -m "uf"
git push origin main

#histogram

years = [2005, 2006, 2007, 2008, 2009]
weight = [40, 50, 60, 70, 80]
plt.hist(years,weight,bins=5)
plt.show()
