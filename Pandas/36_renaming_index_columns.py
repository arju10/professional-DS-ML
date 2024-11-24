
import pandas as pd

# Create dataframe
data = {'Name' : ['Alice', 'Bob'], 'Score': [78,92]}
df = pd.DataFrame(data, index=['Row1','Row2'])


# Renaming index & columns
df_renamed = df.rename(index={'Row1':'Student1', 'Row2':'Student2'}, columns={'Score':'Grade'})

print("Renamed Dataframe : \n",df_renamed)