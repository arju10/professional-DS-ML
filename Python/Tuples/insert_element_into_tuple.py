# Tuple are immutable so element can't be added directly
# However, element can be created by concatenating the existing one with another tuple

# Create tuple 
my_tuple = (1,2,3,'Hello', 4, (10,20))

# Adding elements by creating a new tuple
my_tuple = my_tuple + (100, )


# Print the updated Tuple
print('Updating Tuple: ', my_tuple)
