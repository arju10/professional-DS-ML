import pandas as pd

# Create a dataframe with duplicate rows
data = {'ID':[1,2,2,3,4,4], 'Value': [10, 20,20,30,40,40]}
df = pd.DataFrame(data)

# Detecting duplicates
duplicates = df[df.duplicated()]

print('Duplicate Row : \n', duplicates)