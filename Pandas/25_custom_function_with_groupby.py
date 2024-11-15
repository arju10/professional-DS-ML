import pandas as pd

# Create dataframe
data = {
    'Category':['A','A','B','B'],
    'Value':[10, 20, 30,40]
}

df = pd.DataFrame(data)

# Applying a custom function with groupby
grouped_df = df.groupby('Category') ['Value'].apply(lambda x: x.max() - x.min())

print("Custom Aggregation result : \n", grouped_df)