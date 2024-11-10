import numpy as np

# Create an array
array = np.array(
    [14,1,54,5,125,214,1,2,43,4,2,2,41,14,54,214,1]
)

# Finding Unique Element and their counts
unique_element , counts= np.unique(array, return_counts=True)

print("Unique Elements : ", unique_element)
print("Counts of Unique Elements: ", counts)