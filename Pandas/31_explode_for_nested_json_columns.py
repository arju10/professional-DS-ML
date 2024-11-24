import pandas as pd

# Create a dataframe with nested lists
data = {
    'ID' : [1,2],
    'Hobbies':[['Reading', 'Swimming', 'Gaming'], ['Hiking', 'Drawing']]
}
df = pd.DataFrame(data)

# Exploding the 'Hobbies' column
exploded_df = df.explode('Hobbies')

print("Dataframe after exploding nested json columns:\n", exploded_df)