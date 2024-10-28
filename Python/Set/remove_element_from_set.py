'''
- Using remove() or discard methods a  element can be removed from the set
- remove() method raises an error if the element is not found, while discard() does not.
'''
# Create set 
my_set = {1,2,3,'Hello', 4}

# Removing element using remove() method 
my_set.remove(4)

# Removing element using discard() method (no error if the element is not found)
my_set.discard(4)
#print the created set
print('Set after removal: ', my_set)
