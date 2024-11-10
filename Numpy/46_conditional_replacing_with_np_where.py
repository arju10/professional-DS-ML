import numpy as np

# Create a array
array = np.array(
    [10,20,30,40,60,80]
)

# Replacing values based on condition
result = np.where(array > 25, 0, array)

print("Array with Values where elements > 25 replaced with 0: ",result)