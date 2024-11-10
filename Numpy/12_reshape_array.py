import numpy as np

# Create array
original_array = np.array(
    [1,4,6,7,8,9]
)

# Reshaping to different dimensions
reshaped_array = original_array.reshape((2,3))

print("Original Array : \n", original_array)
print("\n")
print("Reshaping Array : \n", reshaped_array)