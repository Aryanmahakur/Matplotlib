import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random
years = [2010, 2011, 2012, 2014, 2015]
income = [50, 60, 50, 80, 70]

# Define meaningful y-axis ticks within the range of income values
income_ticks = list(range(min(income), max(income) + 10, 10))

plt.plot(years, income, marker='o', linestyle='-')

# Set y-axis tick labels formatted as "50k USD", "60k USD", etc.
plt.yticks(income_ticks, [f"{x}k USD" for x in income_ticks])

plt.xlabel("Years")
plt.ylabel("Income (in thousands of USD)")
plt.title("Yearly Income Progression")

plt.grid(True)  # Adds grid for better visualization
plt.show()

stocka=[100,105,201,111,555]
stockb=[201,43,54,23,50]
stockc=[100,234,50,20,10]
plt.plot(stocka,label="company1")
plt.plot(stockb,label="company2")
plt.plot(stockc,label="company3")
plt.legend(loc="upper left")
plt.show()
