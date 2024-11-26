import pandas as pd

# Create dataframe
data = {'City':['NY', 'LA', 'NY','SF','LA'], 'Year':[2020,2020,2021,2021,2020], 'Sales':[100, 150, 200, 250,300]}
df = pd.DataFrame(data)

# Setting an index
df.set_index('City', inplace=True)
print("Dataframe after setting index: \n", df)
print('\n')
# Resetting index
df.reset_index(inplace=True)
print("Dataframe after resetting index: \n", df)