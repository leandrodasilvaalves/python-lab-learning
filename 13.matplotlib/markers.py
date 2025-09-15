import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints, marker='o')
plt.show()

ypoints= np.array([3,8,1,10])
plt.plot(ypoints, 'o:r')
plt.show()