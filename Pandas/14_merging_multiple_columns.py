import pandas as pd

# Create two dataframe
df1 = pd.DataFrame({'ID':[1,2,3], 'Year':[2020,2021,2023], 'Name':['Alice','Bob','Charlie'] })
df2 = pd.DataFrame({'ID':[2,3,1], 'Year':[2023,2023,2020], 'Score':[88,92,75]})

# Merging on multiple columns
merged_df = pd.merge(df1,df2, on=['ID','Year'], how='inner')

print('Merged Dataframe on multiple columns : \n', merged_df)