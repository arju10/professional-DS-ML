import numpy as np

# Create a 3D array
array_3d = np.array(
    [
        [
            [10,20], [30,40]
        ],
        [
            [50,60], [70,80]
        ]
    ]
)


# Accessing elements in a 3D Array
element = array_3d[1,0,1] # Accessing element at [1, 0 , 1]

# Slicing in 3D
slice_3D = array_3d[:, 0, : ] # First row

print("Element at (1,0,1): ", element)
print("\n")
print("Sliced 3D Array : \n", slice_3D)