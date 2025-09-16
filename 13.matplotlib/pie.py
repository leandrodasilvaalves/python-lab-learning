import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
my_labels = ["apples", "bananas", "cherries", "dates"]

plt.pie(y, labels = my_labels)
plt.legend("4 Fruits")
plt.show()
