'''
- The union() method returns a new set containing all unique elements from both stes
- You can use the | operator to perform the union operation
'''
# Create sets 
my_set = {1,2,3,'Hello', 4}
your_set = {6,7,8, 3}

# Performing Union
union_set = my_set.union(your_set)

#print the union set
print('Union of Set: ', union_set)
