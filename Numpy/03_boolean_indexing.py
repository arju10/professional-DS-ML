import numpy as np

# Create a array
array = np.array(
    [10,20,30,40,60,80]
)

# Boolean Indexing
greater_than_20 = array[array > 20]

print("Elements greater than 20 : ",greater_than_20)