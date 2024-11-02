# Creating a set using comprehension with a condition to filter specific elements

# Create List
numbers = [1,2,3,4,5,66,7,8,9,10]

# Creating a set of even numbers
even_set = {num for num in numbers if num %2 == 0}

print("Set of Even numbers: ", even_set)