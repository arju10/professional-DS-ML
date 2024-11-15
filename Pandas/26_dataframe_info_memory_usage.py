import pandas as pd

# Create dataframe
data = {
    'A': range(1000),
    'B':range(1000, 2000)
}
df = pd.DataFrame(data)

# Displaying dataframe info and memory usage
df_info = df.info(memory_usage='deep')

print('Dataframe info and Memory usage : \n', df_info)