'''
- The difference() method returns a new set containing  elements present in one set but not in the other stes
- You can use the - operator to perform the difference operation

'''
# Create sets 
my_set = {1,2,3,'Hello', 4}
your_set = {6,7,8, 3}

# Performing difference (elements in my_set but not in your_set)
difference_set = my_set.difference(your_set)

#print the difference set
print('difference of Set: ', difference_set)
