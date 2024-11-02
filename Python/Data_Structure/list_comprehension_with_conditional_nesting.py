# using list comprehension with nested loops and conditions to filter elements.

# Create Matrix
matrix = [
    [1,2,3],
    [4,5,7],
    [8,9,10]
]

# Flattening & filtering even numbers from the matrix
even_flattened = [num for row in matrix for num in row if num%2 ==0]

print('Flattened Even Numbers: ', even_flattened)


