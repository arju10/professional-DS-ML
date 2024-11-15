import pandas as pd

# Create dataframe
data = {'A': [1,2,3], 'B':[4,5,6]}
df = pd.DataFrame(data)

# Applying an operation to each element in the Dataframe
df_transformed = df.applymap(lambda x:x**2)

print("Dataframe with squared values : \n", df_transformed)