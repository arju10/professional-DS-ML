import pandas as pd

# Create a dataframe
data = {'A':[1,2,3,4], 'B':[5,6,7,8]}
df = pd.DataFrame(data)

# Using eval for calculations
df['C'] = df.eval('A + B *2')

print("Dataframe with evaluated calculation\n",df) 