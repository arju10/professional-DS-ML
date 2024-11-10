import numpy as np

# Create a 2D array
array_2d = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

# Flattening the array
flattened_array = array_2d.flatten()

print("Flattened Array : ",flattened_array)