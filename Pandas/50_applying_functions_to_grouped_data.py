import pandas as pd

# Create dataframe
data = {
    'Team':['A','A','B','B'],
    'Points':[10, 20, 30,40]
}
df = pd.DataFrame(data)

# Applying a function to grouped data
grouped_df = df.groupby('Team') ['Points'].transform(lambda x: x/x.max() )

print("Dataframe with applied functions to grouped data : \n", grouped_df)