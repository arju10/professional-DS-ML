import pandas as pd
import numpy as np

# Creating dataframe with missing values
data = {'Name':['Alice', 'Bob', np.nan, 'David'], 'Age':[13,np.nan,32,20]}
df = pd.DataFrame(data)

# Filling Missing Values using ffill & bfill
df_ffill = df.fillna(method = 'ffill')
df_bfill = df.fillna(method = 'bfill')



print("Dataframe with forward fill: \n", df_ffill)
print("Dataframe with backwark fill: \n", df_bfill)
