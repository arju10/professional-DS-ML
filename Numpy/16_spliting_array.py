import numpy as np

# create an array
array = np.array(
    [1,2,34,4,5,6]
)

# Spliting the array into three parts
split_arrays = np.array_split(array,3)

print("Original Array :", array)
print("Spiting Array : ", split_arrays)