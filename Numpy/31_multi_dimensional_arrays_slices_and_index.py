import numpy as np

# Create a 2D array
array_2d = np.array(
    [
        [1,2,3,10],
        [4,5,6,11],
        [7,8,9,12]
    ]
)

# Selecting specific rows and columns using slices
selected_slice = array_2d[1:, :2]

print("Selected Slice : \n", selected_slice)