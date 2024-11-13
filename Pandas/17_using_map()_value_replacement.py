import pandas as pd

# Create dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Department':['HR', 'IT', 'Finance']}
df = pd.DataFrame(data)

# Mapping department to codes
department_map = {'HR':1, 'IT':2, 'Finance':3}
df['Dept Code'] = df['Department'].map(department_map)

print("Dataframe with mapped values: \n", df)