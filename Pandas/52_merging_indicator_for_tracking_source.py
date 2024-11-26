import pandas as pd

# Create dataframe
df1 = pd.DataFrame({'ID': [1,2,3,4] ,'Name' : ['Alice', 'Bob', 'Charlie', 'David']})
df2 = pd.DataFrame({'ID': [3,4,5,6] ,'Name' : ['Charlie', 'David','Robin','Michale']})


# Merging with indicator to track the source
merged_df = pd.merge(df1, df2, on='ID', how='outer', indicator=True)

print('Merged dataframe with  indicator: \n', merged_df)


'''
Merged dataframe with  indicator: 
    ID   Name_x   Name_y      _merge
0   1    Alice      NaN   left_only
1   2      Bob      NaN   left_only
2   3  Charlie  Charlie        both
3   4    David    David        both
4   5      NaN    Robin  right_only
5   6      NaN  Michale  right_only
'''