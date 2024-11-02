# creating a  tuple_comprehension_using_generatir_expression for elements that meet a condiotion

# Create range of number
numbers = range(1,11)

# Creating a tuple of squares of even numbers
even_squares = tuple(x**2 for x in numbers if x%2 ==0)

print("Tuple of even squares: ", even_squares)