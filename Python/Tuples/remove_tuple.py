'''
-  Tuple are immutable so element can't be deleted directly
- For remove a element , you have to convert the tuple in list ,remove it and then back to a tuple

'''


# Create tuple 
my_tuple = (1,2,3,'Hello', 4, (10,20))

# Convert a tuple to a list and removing the  elements.
conv_list = list(my_tuple) # Conver from Tuple to List
conv_list.remove(2) # Delete the element
my_tuple = tuple (conv_list) # Conver from List  to Tuple


# Print the updated Tuple
print('Updating Tuple after removing: ', my_tuple)
