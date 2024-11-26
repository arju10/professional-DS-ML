import pandas as pd

# Create dataframe
data = {'Score': [85, 70, 95,60, 100, 90]}
df = pd.DataFrame(data)

# Binning the scores into categories
df['Grade'] = pd.cut(df['Score'], bins=[0,59,69,79,89,100], labels=['F', 'D', 'C', 'B','A'])

print('Dataframe with binned scores : \n', df)