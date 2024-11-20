import pandas as pd

# Create dataframe
data = {'Name' : ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85,90,78,92], 'Age': [25,37,35,21]}
df = pd.DataFrame(data)

# Sorting by multiple columns
sorted_df = df.sort_values(by=['Score', 'Age'], ascending=[False, True])

print("Sorted Dataframe by multiple columns: \n", sorted_df)


