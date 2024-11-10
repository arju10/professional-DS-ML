import numpy as np

# Create a 2D array
array_2d = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

# Multi Dimensional Slicing
sub_array = array_2d[1:, 1:3]

print("Sub Array (Slicing Rows & Columns) : \n", sub_array)