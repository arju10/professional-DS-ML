import pandas as pd

# Create dataframe
data = {'Name' : ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85,90,78,92]}
df = pd.DataFrame(data)

# Use query for filtering
filtered_df = df.query('Score > 80')

print('Filtered dataframe using query : \n', filtered_df)