import numpy as np

# Create a array
array = np.array([1,2,4,5])

# Clipping values to be between 2 and 4
clipped_array = np.clip(array, 2,4)

print("Original Array",array)
print("Clipped Array",clipped_array)
