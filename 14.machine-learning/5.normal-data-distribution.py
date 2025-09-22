# https://www.w3schools.com/python/python_ml_normal_data_distribution.asp

import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(5.0, 1.0, 100_000)

plt.hist(x, 100)
plt.show()
