import pandas as pd

# Create dataframe
data = {'Sales': [100, 200, 150, 300, 250]}
df = pd.DataFrame(data)

# Calculating cumulative sum and product
df['cumulative sum'] = df['Sales'].cumsum()
df['cumulative product'] = df['Sales'].cumprod()

print('DataFrame with cumulative operations:\n', df)