import pandas as pd

# Create a dataframe with duplicate rows
data = {'ID':[1,2,2,3,4,4], 'Value': [10, 20,20,30,40,40]}
df = pd.DataFrame(data)

# Dropping duplicates rows
unique_df = df.drop_duplicates()

print("Dataframe after dropping duplicates: \n", unique_df)