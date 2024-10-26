'''
- Remove the key-value pair using pop() method is a method which removes the specified key and returns its value 

'''

# Create a Dictionary named people_info with various key-value-pairs
people_info = {'name':'John', 'age':25, 'city':"New York"}

# Removing a key-value pair
age = people_info.pop('age')

# Print the  dictionary after removing
print("Dictionary After removal: ", people_info)
print("Removed Age: ", age)