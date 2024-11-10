# Numpy - 2D Array indexing

import numpy as np

# Create a 2D array
array_2d = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

# Using arrays for indexing
rows = np.array([0,1,2]) 
cols = np.array([2,1,0])
indexed_elements = array_2d[rows, cols]

print("Indexed Elements : ", indexed_elements)
