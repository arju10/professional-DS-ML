import pandas as pd

# Create a multi-index from tuple
index = pd.MultiIndex.from_tuples([('A',2020), ('A', 2021), ('B', 2021), ('C', 2022)], names=['Category', 'Year'])
data = [100, 150, 200, 250]
df = pd.DataFrame(data, index=index, columns=['Sales'])

print("Dataframe with custom multi-index: \n", df)
