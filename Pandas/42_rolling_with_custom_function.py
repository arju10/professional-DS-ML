import pandas as pd

# Create a time series dataframe
data_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales': [100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}
df = pd.DataFrame(data, index= data_range)

# Applying a custom function with rolling()
df['Rolling Sum'] = df['Sales'].rolling(window=3).apply(lambda x:x.sum() if x.sum() > 50 else 0)

print("Dataframe with custom rolling sum : \n", df)