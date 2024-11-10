import numpy as np

# Create a square Matrix
matrix = ([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Extracting the main diagnal
diagnoal_elements = np.diag(matrix)

print("Diagnoal Elements: ", diagnoal_elements)