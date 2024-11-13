import pandas as pd

# Create a Data Frame
data = {'Category':['A', 'B', 'C', 'A','B','C','C','A'],
        'Value':[10, 20, 40, 45, 50, 90,100, 200]}

df = pd.DataFrame(data)


# Grouping by 'category' and calculating the sum and mean
grouped = df.groupby('Category').agg({'Value': ['sum', 'mean']})

print("Grouped Data Frame with Aggregation: \n\n", grouped)