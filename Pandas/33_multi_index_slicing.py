import pandas as pd

# Create Multi Index Dataframe
arrays = [['A', 'A', 'B', 'B'], [2020, 2021, 2022, 2023]]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Year'))
data = [100, 150, 200, 250]
df = pd.DataFrame(data, index=index, columns=['Sales'])

# Slicing the  mutiindex Dataframe
sliced_df = df.loc['A']

print("Sliced  mutiindex Dataframe \n", sliced_df)