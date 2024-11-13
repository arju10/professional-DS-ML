import pandas as pd

# Create Dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score':[85,90,95]}
df = pd.DataFrame(data)

# Applying a lambda function to modify scores
df['Adjusted Score'] = df['Score'].apply(lambda x: x+5 if x<90 else x)

print("Dataframe with Adjusted Scores :\n",df)
