import numpy as np

# Create a array
array = np.array(
    [1,2,3,4,5,6]
)

# Setting elements that satisfying a condition
array[array % 2 == 0] = -1 # Set even numbers to -1

print("Array after conditional indexing : ",array)