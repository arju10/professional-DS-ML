'''
- Using add() method a new element can be added
- Sets do not allow duplicate elements.
'''
# Create set 
my_set = {1,2,3,'Hello', 4}

# Adding new element
my_set.add(4)

# Trying to add duplicate element
my_set.add(2)
#print the created set
print('Updated Set: ', my_set)
