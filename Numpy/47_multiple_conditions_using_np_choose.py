import numpy as np

# Create an array
array = np.array([1, 2, 4, 5])

# Extend choices to include placeholder arrays for out-of-bounds indices
choices = [array * 2, array + 10, array ** 2, array * 0, array * 0, array * 0]

# Use np.choose with the modified choices array
result = np.choose(array, choices)

print("Result using np.choose:", result)
