import numpy as np

# Create array
array = np.array([1,-2,3,-4,5])

# Creating a Mask for positive values
mask = array > 0

# Applyinh mask to get only positive values
positive_values = array[mask]

print("Positive Values : ", positive_values)