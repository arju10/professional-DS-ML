'''
- Tuple do not support comprehension like list
- However, you can use a generator expression to create a tuple
'''

# Create a tuple of squre of numbers from 0 to 4
squre_tuple = tuple(x**2 for x in range(5))

# Print the  tuple
print("Squre tuple: ", squre_tuple)
