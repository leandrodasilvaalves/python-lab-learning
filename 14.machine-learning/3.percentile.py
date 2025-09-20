import numpy as np

# https://www.w3schools.com/python/python_ml_percentile.asp
ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]
x = np.percentile(ages, 75)
print("percentile:", x)


# https://chatgpt.com/c/68cf1481-1370-8327-b6cf-00dadcd19015
def calc_percentile(values, percent):
    ordered = sorted(values)
    size = len(ordered)
    position = (size - 1) * percent / 100
    lower_index = int(position)
    fraction = position - lower_index

    print(ordered)
    print("size:", size)
    print("position:", position)
    print("lower_index:", lower_index)
    print("fraction:", fraction)

    if fraction == 0:
        return ordered[lower_index]
    else:
        a = ordered[lower_index] * (1 - fraction)
        b = ordered[lower_index + 1] * fraction
        print("interpolation:", {a, b})
        return a + b


x = calc_percentile(ages, 75)
print("percentile:", x)

x = calc_percentile(ages, 62.5)
print("percentile:", x)
