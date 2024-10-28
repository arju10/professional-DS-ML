'''
- Tuple is immutable (can't be changed) which means their values can't be changed after creating
'''
# Create tuple 
my_tuple = (1,2,3,'Hello', 4, (10,20))

# Trying to modify the tuple, it will show error

try:
    my_tuple[0] = 10
except TypeError as e:
    print('Error',e)

