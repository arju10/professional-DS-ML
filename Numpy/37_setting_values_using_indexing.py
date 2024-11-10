import numpy as np

# Create a array
array = np.array(
    [1,2,3,4,5,6]
)

# Setting specific values using indexing
array[[1,3]] = [100, 200]

print("Array after Setting value :", array)