import pandas as pd

# Create dataframe
data = {'City': ['NY', 'LA', 'SF', 'NY']}
df = pd.DataFrame(data)

# Creating dummy varibales
dummies = pd.get_dummies(df['City'], prefix='City')

print('Dummy varibales dataframe: \n', dummies)