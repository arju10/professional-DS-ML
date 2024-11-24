import pandas as pd

# Create dataframe
data = {'Name' : ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85,90,78,92], 'Age': [25,37,35,21]}
df = pd.DataFrame(data)

# Using query() with varibales
threshold = 80
filtered_df = df.query('Score > @threshold')

print("Filtered Dataframe with query() and varibales: \n", filtered_df)