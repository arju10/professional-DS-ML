import numpy as np

# Create array
array = np.array([1,-2,3,-4,5])

# Masking elements where values are negative
masked_array = np.ma.masked_where(array < 0, array)

print("Masked Array with negative values hidden: ", masked_array)