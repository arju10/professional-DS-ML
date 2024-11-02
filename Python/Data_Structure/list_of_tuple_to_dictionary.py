# Converting a list of tuple into a dictionary using loop

# Create list of tuple
tuple_list = [('a',1), ('b',2), ('c',3), ('d',5)]

# Converting to a dictionary

result_dict = {key:value for key, value in tuple_list}

print("Dictionary from list of tuples: ", result_dict)