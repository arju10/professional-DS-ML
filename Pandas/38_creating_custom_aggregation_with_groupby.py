import pandas as pd

# Create dataframe
data = {
    'Category':['A','A','B','B'],
    'Value':[10, 20, 30,40]
}

df = pd.DataFrame(data)

# Using groupby with custom aggregation
custom_df = df.groupby('Category').agg(max_value = ('Value', 'max'), min_value=('Value', 'min'))

print("Custom Aggregation result : \n", custom_df)