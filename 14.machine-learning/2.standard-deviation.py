# https://www.w3schools.com/python/python_ml_standard_deviation.asp

# Standard deviation is a number that describes how spread out the values are.

import numpy as np
import math

speed = [86, 87, 88, 86, 87, 85, 86]
deviation = np.std(speed)
print("deviation: ", deviation)

variance = np.var(speed)
print("variance:", variance)

# que tal calcular o desvio manualmente 
# pra entender o que acontece aqui?
# https://chatgpt.com/c/68cd20a5-46e4-8333-8f99-861ca963717e

def calculate_deviation(speed):
    print(''.rjust(50,'-'))
    speed_count = len(speed)
    speed_sum = 0

    for sp in speed:
        speed_sum += sp

    speed_mean = speed_sum / speed_count

    print("sum:", speed_sum)
    print("count:", speed_count)
    print("mean:", speed_mean)

    # print("")
    # print("deviations")
    deviations = []
    for sp in speed:
        dev = sp - speed_mean
        deviations.append(sp - speed_mean)
        # print(" ", dev)

    # print("")
    # print("squared deviations")
    squared_deviations = []
    squared_sum = 0
    for dev in deviations:
        squared = math.pow(dev, 2)
        squared_deviations.append(squared)
        squared_sum += squared
        # print(" ", squared)

    print("squared sum:", squared_sum)

    variance = squared_sum / speed_count
    print("variance:", variance)

    std_deviation = math.sqrt(variance)
    print("standard deviation:", std_deviation)

    print("analyzing standard deviation")
    result = (std_deviation / speed_mean) * 100
    if result < 10:
        print("Safe - stable variation:", result)
    elif result >= 10 and result < 20:
        print("Warning - medium variation:", result)
    else:
        print("Danger - high variation:", result)


calculate_deviation([86, 87, 88, 86, 87, 85, 86])
# calculate_deviation([60, 90, 88, 75, 87, 98, 60])
# calculate_deviation([20, 87, 55, 86, 10, 85, 120])

