import pandas as pd

# Create dataframe
data = {'Name':['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 70, 95,60]}
df = pd.DataFrame(data)

# Creating a new column with categorical data
df['Performance'] = pd.cut(df['Score'], bins=[0,70,90,100], labels=['Poor', 'Average', 'Excellent'])

print('Dataframe with categorical performance : \n', df)