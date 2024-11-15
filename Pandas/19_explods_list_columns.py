import pandas as pd

# Create a dataframe with lists in a column
data = {'ID':[1,2], 'Hobbies':[['Reading', 'Swimming'], ['Running', 'Cycling'] ]}
df = pd.DataFrame(data)

# Explodeing the 'Hobbies' Column
exploded_df = df.explode('Hobbies')

print("Dataframe after exploring lists: \n", exploded_df)