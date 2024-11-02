'''
Unpacking a tuple with multiple values into variables, including using the * operator for remaining values.
'''

# Create Tuple
person_info = ('John', 25, 'New York', 'Engineer', 'Single')

# Unpacking tuple into variable
name, age, *other_details = person_info

print("Name: ",name)
print("Age : ",age)
print("Other details: ", other_details)