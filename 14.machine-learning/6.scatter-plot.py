# https://www.w3schools.com/python/python_ml_scatterplot.asp
import numpy as np
import matplotlib.pyplot as plt

# x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
# y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# plt.scatter(x, y)
# plt.show()

# Scatter Plot Explained
# ----------------------
# The x-axis represents ages, and the y-axis represents speeds.

# What we can read from the diagram is that the two fastest cars were
# both 2 years old, and the slowest car was 12 years old.

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()
