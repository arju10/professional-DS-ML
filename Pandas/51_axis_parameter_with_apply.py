import pandas as pd

# Create dataframe
data = {'A': [1,2,3], 'B':[4,5,6]}
df = pd.DataFrame(data)

# Applying a function to rows and columns using the axis parameter
row_sum = df.apply(lambda x: x.sum() , axis=1)
col_sum = df.apply(lambda x: x.sum() , axis=0)

print("Row wise sum : \n", row_sum)
print("Column wise sum : \n", col_sum)
