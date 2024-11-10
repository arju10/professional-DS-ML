import numpy as np

# Creating a 2D array
array_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Applying boolean indexing first, then fancy indexing and slicing
result = array_2d[array_2d > 30].reshape(-1, 3)[:, [0, 2]]

print('Combined Indexing Result:', result)
