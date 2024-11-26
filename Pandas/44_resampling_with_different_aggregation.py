import pandas as pd

# Create time Series Dataframe
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales':[100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}
df = pd.DataFrame(data, index=date_range)

# Resampling to find weekly sales
resampled_df = df.resample('W').agg({'Sales':['sum', 'mean', 'max']})

print("Resampled Dataframe with different aggregation : \n", resampled_df)