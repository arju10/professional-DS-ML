import pandas as pd

# Create dataframe
data = {'Value': [10, 12, 14, 100, 15, 13, 12]}
df = pd.DataFrame(data)

# Indentifying outliers using the IQR method
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Value'] < (Q1 - 1.5 * IQR)) | (df['Value'] > (Q3 + 1.5 * IQR))]

print('Outliers: \n', outliers)