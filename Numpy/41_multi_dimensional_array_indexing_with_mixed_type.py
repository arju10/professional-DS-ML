import numpy as np

# Create 3D Array
array_3D = np.array([
        [[1,2], [3,4]], [[5,6], [7,8]], [[9,10], [11,12]]
]
)

# Mixing slicing with direct indexing
mixed_index = array_3D[1:, 0, 1]

print("Mixed type indexing result: ", mixed_index)