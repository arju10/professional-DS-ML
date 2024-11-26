import pandas as pd

# Create dataframe
data = {'City':['NY', 'LA', 'NY','SF','LA'], 'Year':[2020,2020,2021,2021,2020], 'Sales':[100, 150, 200, 250,300]}
df = pd.DataFrame(data)

# Create a pivot table with multiple indexes
pivot_table = pd.pivot_table(df, values='Sales', index=['City', 'Year'], aggfunc='sum')

print('Pivot table with multiple indexes: \n', pivot_table)