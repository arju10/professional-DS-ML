import pandas as pd

# Create Dataframe
data = {'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
        'Sales': [300, 302, 305,303, 310]}

df = pd.DataFrame(data)

# Shifting data by one to create a lag
df['Prev Day Sales'] = df['Sales'].shift(1)

print('Dataframe with shifted data: \n', df)