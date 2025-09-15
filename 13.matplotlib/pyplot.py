import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints, marker='o')
plt.show()

ypoints= np.array([3,8,1,10])
plt.plot(ypoints, 'o:r')
plt.show()