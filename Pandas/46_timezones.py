import pandas as pd

# Create a time series dataframe
data_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales': [100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}
df = pd.DataFrame(data, index=data_range)

# Localizing the timezone to UTC (or any initial timezone)
df.index = df.index.tz_localize('UTC')

# Converting to a different timezone (US/Eastern)
df = df.tz_convert('US/Eastern')

print("Time series dataframe with time zone: \n", df)
