'''
Working with nested lists by accessing elements, modifying values, and flattening the list.
'''

# Create Nested List
nested_list = [
    [1,2,3],
    [4,5,[6,7]],
    [8,9]
]

# Accessing the nested list
nested_element = nested_list[1][2][1] # Accessing 7

# Modifying nested element
nested_list[2][1] = 10 # Changin 9 to 10

# Flattening the nested list
flattened_list = [element for sublist in nested_list for item in sublist for element in (item if isinstance(item,list) else[item])]

print('Nested ELement :',nested_element)
print('Modified Nested List : ', nested_list)
print('Flattended List : ', flattened_list)