'''
- The symmetric_difference() method returns a new set containing  elements present in either set but not in both stes
- You can use the ^ operator to perform the symmectric difference operation.

'''
# Create sets 
my_set = {1,2,3,'Hello', 4}
your_set = {6,7,8, 3}

# Performing symmetric_difference (elements in my_set but not in your_set)
symmetric_difference_set = my_set.symmetric_difference(your_set)

#print the symmetric_difference set
print('symmetric_difference of Set: ', symmetric_difference_set)
