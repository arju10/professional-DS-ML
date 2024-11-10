import numpy as np

# Create a square Matrix
matrix = ([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Extracting the upper triangle (above the main diaginal)
upper_triangle = np.triu(matrix)

print("Upper Triangle of the Matrix: \n", upper_triangle)