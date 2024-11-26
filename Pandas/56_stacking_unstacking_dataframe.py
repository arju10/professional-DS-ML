import pandas as pd

# Create dataframe
data = {'City':['NY','LA'],
        '2020':[100,500],
        '2021':[200,450],
        }

df = pd.DataFrame(data)

# Stacking & Unstacking dataframe
stack_df = df.stack()
unstack_df = df.unstack()

print('Stacking dataframe \n', stack_df)
print('Unstacking dataframe \n', unstack_df)
