import pandas as pd

# Create dataframe
data = {'Name' : ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85,90,78,92]}
df = pd.DataFrame(data)

# Adding a new column using assign
df = df.assign(Grade= lambda x: ['A' if Score >= 90 else 'B' for Score in x['Score']])

print("Dataframe with assigned grade column : \n", df)