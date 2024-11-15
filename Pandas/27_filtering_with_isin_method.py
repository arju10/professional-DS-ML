import pandas as pd

# Create dataframe
data = {'Name' : ['Alice', 'Bob', 'Charlie', 'David'], 'City': ['NY','LA','SF','NY']}
df = pd.DataFrame(data)

# filter with isin()
filtered_df = df[df['City'].isin(['NY','SF'])]

print("Filtered Dataframe with isin method: \n", filtered_df)
