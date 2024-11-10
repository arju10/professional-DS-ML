import numpy as np

# Create a 3D array
array_3D = np.array(
    [[
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10],
        [11,12]
    ]]
)

# Using Ellipisis to seletect all elements along axes
result = array_3D[..., 1] # Selecting the second column in each 2D Slices

print("Result using Ellipsis (...): \n", result)