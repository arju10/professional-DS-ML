import pandas as pd

# Create dataframe
data = {'ID':[1,2], 'Math':[90,79], 'Science':[85,88]}
df = pd.DataFrame(data)

# Melting the dataframe
melted_dataframe = pd.melt(df,id_vars=['ID'], var_name='Subject', value_name='Score')

print("Melted Dataframe : \n", melted_dataframe)