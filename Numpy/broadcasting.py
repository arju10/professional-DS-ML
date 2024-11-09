import numpy as np

# create array
array = np.array(
    [1,2,3]
)

# Braodcasting: Adding a scaler to an array
result = array + 10

print("Original Array: ", array)
print("Array after broadcasting : ", result)