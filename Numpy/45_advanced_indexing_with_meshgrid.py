import numpy as np

# Create arrays
x = np.array([1,2,3])
y = np.array([4,5,6])

# Create a meshgrid
x,y = np.meshgrid(x,y)

indices = np.vstack(
    [x.ravel(), y.ravel()]
)

print("Indices for Meshgrid Advanced Indexing: \n", indices)