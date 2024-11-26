import pandas as pd

# Create dataframe
data = {
    'Category':['A','A','B','B'],
    'Values':[10, 20, 30,40]
}
df = pd.DataFrame(data)

# Grouping by 'category' and calculating the sum and mean
grouped_df = df.groupby('Category').agg({'Values': ['sum', 'mean','max']})

print("Grouped Data Frame with with multiple functions \n\n", grouped_df)