import pandas as pd

# Create dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 90, 78, 92]}
df = pd.DataFrame(data)

# Custom function for modifying the dataframe
def add_grade_column(df):
    df['Grade'] = df['Score'].apply(lambda x: 'A' if x >=90 else 'B')
    return df

# Using pipe() for method chaining
df = df.pipe(add_grade_column)

print("Dataframe after using pipe : \n", df)