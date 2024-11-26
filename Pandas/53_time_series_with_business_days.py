import pandas as pd

# Create a time series dataframe
data_range = pd.date_range(start='2023-01-01', periods=10, freq='B')
data = {'Sales': range(10)}
df = pd.DataFrame(data, index= data_range)

print("Time series Dataframe with business days : \n", df)

