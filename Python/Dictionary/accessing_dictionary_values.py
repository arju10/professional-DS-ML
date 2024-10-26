'''

- Values in a Dictionary are accessed using their keys.
- If a key is not found, a keyError will be raised unless you use the get() method, which returns None.

'''

# People Information as Dictionary format
people_info = {'name':'John', 'age':25, 'city':"New York"}

# Accessing dictionary values using keys
name = people_info['name']
age = people_info.get('age')

# Print the accessed values
print('Name : ', name)
print('Age : ', age)