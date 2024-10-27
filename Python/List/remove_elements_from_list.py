'''
- remove() and pop() is used for remove elements from list
- remove() deletes the first occurance of a value
- pop() removes an element by index.

'''

# Create a list with various data types
my_list = [10, 20, 30,40, 50]

# Remove the  elements
my_list.remove(50)
popped_item = my_list.pop(2)

# Print the modified list
print("List After removal: ", my_list)
print("Popped Item : ", popped_item)