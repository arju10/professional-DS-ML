'''
- Tuple are immutable so element can't be soting directly
- For sorting a tuple , you have to convert the tuple in list ,sort it and then back to a tuple
'''

# Create tuple 
my_tuple = (1,2,3, 4)

# Convert a tuple to a list and removing the  elements.
# Sort by ascending order
sorted_list = sorted(my_tuple)
my_tuple = tuple(sorted_list)

# Print the sorted Tuple
print("Sorted tuple : ", my_tuple)

