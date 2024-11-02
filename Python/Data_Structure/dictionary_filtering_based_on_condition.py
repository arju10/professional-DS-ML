# Filtering a dictinary a retain only key-value pairs that satisfy a conditions

# Create a dictionary
scores = {
    'Alice':93,
    'Boby':53,
    'Charlie':52,
    'David': 40
}

# Filtering to retain scores >= 80
filtered_scores = {
    name : score for name, score in scores.items() 
    if score >=80
}

print('Filtered Score :', filtered_scores)