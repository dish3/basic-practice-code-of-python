from scipy import constants

print(constants.pi)  # Output: 3.141592653589793
print(constants.c)   # Speed of light in m/s

import math

print(math.sqrt(25))  # Output: 5.0
print(math.factorial(5))  # Output: 120
print(math.ceil(4.2))  # Output: 5
print(math.floor(4.8))  # Output: 4

import numpy as np

arr = np.array([1, 2, 3])
print(arr * 2)  # Output: [2 4 6]

import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)

print(df)


import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker="o")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")
plt.show()

