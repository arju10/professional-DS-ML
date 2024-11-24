import pandas as pd

# Create a dataframe
data = {
    'Math': [90, 80],
    'Science':[85,88]
}
df = pd.DataFrame(data)

# Adding prefix to column names
df_prefixed = df.add_prefix('Grade_')

# Adding suffix to column names
df_suffixed = df.add_suffix('_Score')

print("Dataframe with Prefix :\n", df_prefixed)
print('\n')
print("Dataframe with Suffix :\n", df_suffixed)
