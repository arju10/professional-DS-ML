import pandas as pd

# Create dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score':[85, 80,40,70], 'Passed':[True, False, True, False]}
df = pd.DataFrame(data)

# Filtering with multiple conditions
filtered_df = df[(df['Score'] > 80) & (df['Passed'] == True)]

print("FIltered Dataframe : \n", filtered_df)