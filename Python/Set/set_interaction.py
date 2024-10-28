'''
- The intersection() method returns a new set containing common elements from both stes
- You can use the & operator to perform the intersection operation

'''
# Create sets 
my_set = {1,2,3,'Hello', 4}
your_set = {6,7,8, 3}

# Performing intersection
intersection_set = my_set.intersection(your_set)

#print the intersection set
print('intersection of Set: ', intersection_set)
