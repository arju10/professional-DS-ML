# Accessing and modifying elements in a dictionary with need structures

# Create dictionary with nested structures
nested_dic = {
    'person': {
        'name':'John',
        'details':{
            'age':234,
            'city':'New York',
            'skills':['Python',"Data Analysis"]
        }
    }
}

# Accessing nested elements
city = nested_dic['person']['details']['city']

# Modifying a nested element
nested_dic['person']['details']['skills'].append('Machine Learning')

print('City: ', city)
print('Updated nested dictionary: ', nested_dic)