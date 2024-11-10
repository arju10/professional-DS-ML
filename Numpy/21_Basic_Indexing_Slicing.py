import numpy as np

# Create a array
array = np.array([1,2,4,5])

# Aceesing element by index
first_element = array[0]
last_element = array[-1]

# Slicing the array
slice_array = array[1:4]

print("First Element: ", first_element)
print("Last Element: ", last_element)
print("Sliced Element: ", slice_array)