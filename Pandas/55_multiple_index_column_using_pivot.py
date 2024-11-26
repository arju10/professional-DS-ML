import pandas as pd

# Create dataframe
data = {'Date':['2023-01-01', '2023-01-02','2023-01-01','2023-01-02'],
        'City':['NY', 'NY','LA', 'LA'],
        'Type': ['Online', 'Store', 'Online','Store'],
        'Sales':[200,250,300,400]
        }

df = pd.DataFrame(data)

# Pivoting to create a Dataframe with multi-index columns
pivot_df = df.pivot(index='Date', columns=['City','Type'], values='Sales')

print('Pivoted Dataframe with multi-index columns: \n', pivot_df)