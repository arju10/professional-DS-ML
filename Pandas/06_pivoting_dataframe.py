import pandas as pd

# Create dataframe
data = {'Date':['2023-01-01', '2023-01-02','2023-01-01','2023-01-02'],
        'City':['NY', 'NY','LA', 'LA'],
        'Sales':[200,250,300,400]
        }

df = pd.DataFrame(data)

# Pivoting the Dataframe
pivot_df = df.pivot(index='Date', columns='City', values='Sales')

print('Pivoted Dataframe : \n', pivot_df)


