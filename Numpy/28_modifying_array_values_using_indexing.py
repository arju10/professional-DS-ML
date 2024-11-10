import numpy as np

# Create a array
array = np.array([1,2,4,5])

#Modifying values specific indices
array[[1,3]] = [100, 200]

print("Modified Array : ",array)