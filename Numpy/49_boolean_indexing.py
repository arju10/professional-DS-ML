import numpy as np

# Create a array
array = np.array(
    [10,20,30,40,60,80]
)

# Boolean Indexing
even_numbers = array[array %2==0]

print("Original : ", array)
print("Even Numbers : ",even_numbers)