import pandas as pd

# Create two dataframe
df1 = pd.DataFrame({'ID':[1,2,3], 'Name':['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'Emp_ID':[2,3,4], 'Department':['HR','Finance','IT']})

#Merging with different keys
merged_df = pd.merge(df1, df2, left_on='ID', right_on='Emp_ID', how='outer')

print("Merged Dataframe: \n", merged_df)