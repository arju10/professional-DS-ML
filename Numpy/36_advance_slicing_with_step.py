import numpy as np

# Create a 2D Array
array_2d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Slicing every second element in rows and columns
step_sliced_element = array_2d[::2, ::2]

print("Advanced sliced array with step \n", step_sliced_element)