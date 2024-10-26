# Merge the dictionaries using update() method or ** operator in Python 3.9+.

# Create a Dictionaries
people_info = {'name':'John', 'age':25}
address_info = {'city':'New York', 'country':'USA'}

# Merging dictionaries
people_info.update(address_info)

# Print the merge dictionary
print("Created Dictionary", people_info)