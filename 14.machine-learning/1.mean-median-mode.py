# https://www.w3schools.com/python/python_ml_mean_median_mode.asp

import numpy as np

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print("mean: ", x)

# The median value is the value in the middle, after you have sorted all the values:
x = np.median(speed)
print("median: ", x)

speed2 = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]
# (86 + 87) / 2 = 86.5
x = np.median(speed2)
print("median: ", x)

#The Mode value is the value that appears the most number of times
from scipy import stats
x = stats.mode(speed)
print("mode: ", x)