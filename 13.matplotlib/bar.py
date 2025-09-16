# https://www.w3schools.com/python/matplotlib_bars.asp

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()

plt.bar(x,y, color="red", width=0.5)
plt.show()