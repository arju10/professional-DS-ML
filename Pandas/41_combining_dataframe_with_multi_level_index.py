import pandas as pd

# Create Multi Index Dataframe
arrays = [['A', 'A', 'B', 'B'], [2020, 2021, 2022, 2023]]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Year'))
data1 = [100, 150, 200, 250]
df1 = pd.DataFrame(data1, index=index, columns=['Sales'])

data2 = [300, 400, 500, 6000]
df2 = pd.DataFrame(data2, index=index, columns=['Profit'])

# Combining Dataframe
combined_df = pd.concat([df1, df2], axis=1)

print("Combining Dataframe with Multi-level Indexes: \n ", combined_df)