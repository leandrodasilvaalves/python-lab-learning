# https://www.w3schools.com/python/python_ml_data_distribution.asp

import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 5.0, 250)
print(x)

plt.hist(x,5)
plt.show()