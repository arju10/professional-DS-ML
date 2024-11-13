# Pandas

### Grouping & Aggregation

Grouping data frame using aggregation functions, including `sum` and `mean`, calculated per category.

```python
## Numpy
import pandas as pd

# Create a Data Frame
data = {'Category':['A', 'B', 'C', 'A','B','C','C','A'],
        'Value':[10, 20, 40, 45, 50, 90,100, 200]}

df = pd.DataFrame(data)


# Grouping by 'category' and calculating the sum and mean
grouped = df.groupby('Category').agg({'Value': ['sum', 'mean']})

print("Grouped Data Frame with Aggregation: \n\n", grouped)
```

***Output:***

`Grouped Data Frame with Aggregation:` </br> 
| Category | Value (sum) | Value (mean) |
|----------|-------------|--------------|
| A        | 255         | 85.000000    |
| B        | 70          | 35.000000    |
| C        | 230         | 76.666667    |


Here,the data is grouped by `Category`, and for each category, we calculate:
- **Sum** of the `Value` column
- **Mean** of the `Value` column

### Explanation of Columns:
- **Category**: The category label for each group.
- **Value (sum)**: The total sum of values within each category.
- **Value (mean)**: The average value within each category.

### MutiIndex DataFrame Operations

```python
import pandas as pd

# Create Multi Index Dataframe
arrays = [['A', 'A', 'B', 'B'], [2020, 2021, 2022, 2023]]
index = pd.MultiIndex.from_arrays(arrays, names=('Category', 'Year'))
data = [100, 150, 200, 250]
df = pd.DataFrame(data, index=index, columns=['Sales'])

# Accessing data in a mutiindex Dataframe
sales_in_2020 = df.xs(2020, level='Year')

print("Sales Data in 2020: ", sales_in_2020)
```
***Output***
| Category | Sales (2020) |
|----------|--------------|
| A        | 100          |

Here, output for sales data in `2020`, showing the total sales for each category.


### Using Apply with Lambda Functions

```python
import pandas as pd

# Create Dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Score':[85,90,95]}
df = pd.DataFrame(data)

# Applying a lambda function to modify scores
df['Adjusted Score'] = df['Score'].apply(lambda x: x+5 if x<90 else x)

print("Dataframe with Adjusted Scores :\n",df)
```
***Output***
| Name     | Score | Adjusted Score |
|----------|-------|----------------|
| Alice    | 85    | 90             |
| Bob      | 90    | 90             |
| Charlie  | 95    | 95             |

Here, this data frame includes a list of names, their original scores, and the adjusted scores:

### Merging DataFrame with Different Keys
```python
import pandas as pd

# Create two dataframe
df1 = pd.DataFrame({'ID':[1,2,3], 'Name':['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'Emp_ID':[2,3,4], 'Department':['HR','Finance','IT']})

#Merging with different keys
merged_df = pd.merge(df1, df2, left_on='ID', right_on='Emp_ID', how='outer')

print("Merged Dataframe: \n", merged_df)
```
***Output***
| ID  | Name    | Emp_ID | Department |
|-----|---------|--------|------------|
| 1.0 | Alice   | NaN    | NaN        |
| 2.0 | Bob     | 2.0    | HR         |
| 3.0 | Charlie | 3.0    | Finance    |
| NaN | NaN     | 4.0    | IT         |

Here, the merged data frame combines two data sources, which may contain missing values
- **ID**: Identifier from the first data source.
- **Name**: Name from the first data source.
- **Emp_ID**: Employee ID from the second data source.
- **Department**: Department from the second data source.
- **NaN** values indicate missing data from one of the sources.

### Handling Missing Values with Custom Functions
```python
import pandas as pd
import numpy as np

# Creating dataframe with missing values
data = {'Name':['Alice', 'Bob', np.nan, 'David'], 'Age':[13,np.nan,32,20]}
df = pd.DataFrame(data)

# Filling Missing Values using a custom function
df['Name'].fillna('Unknown', inplace=True)
df['Age'].fillna(df['Age'].median(), inplace=True)

print("Dataframe after handling Missing values: \n", df)
```
***Output***
`Dataframe after handling Missing values:` </br>
| Name    | Age  |
|---------|------|
| Alice   | 13.0 |
| Bob     | 20.0 |
| Unknown | 32.0 |
| David   | 20.0 |

Here,missing values in the `Name` or `Age` columns were replaced with a default string (`"Unknown"`) or a specified numeric value.

### Pivoting DataFrame
```python
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
```
***Output***

`Pivoted Dataframe :` </br>
| Date       | LA   | NY   |
|------------|------|------|
| 2023-01-01 | 300  | 200  |
| 2023-01-02 | 400  | 250  |

### Melting DataFrame
```python
import pandas as pd

# Create dataframe
data = {'ID':[1,2], 'Math':[90,79], 'Science':[85,88]}
df = pd.DataFrame(data)

# Melting the dataframe
melted_dataframe = pd.melt(df,id_vars=['ID'], value_vars=['Math', 'Science'], var_name='Subject', value_name='Score')

print("Melted Dataframe : \n", melted_dataframe)
```
***Output***

`Melted DataFrame :` </br>

| ID  | Subject | Score |
|-----|---------|-------|
| 1   | Math    | 90    |
| 2   | Math    | 79    |
| 1   | Science | 85    |
| 2   | Science | 88    |

### Time based indexing and resampling
```python
import pandas as pd

# Create time Series Dataframe
date_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales':[100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}
df = pd.DataFrame(data, index=date_range)

# Resampling to find weekly sales
weekly_sales = df.resample('W').sum()

print("Weekly Sales : \n", weekly_sales)
```
***Output***

`Weekly Sales :` </br>

| Date       | Sales |
|------------|-------|
| 2023-01-01 | 100   |
| 2023-01-08 | 1950  |
| 2023-01-15 | 700   |

### Conditional Filtering with Multiple Conditions
```python
import pandas as pd

# Create dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Score':[85, 80,40,70], 'Passed':[True, False, True, False]}
df = pd.DataFrame(data)

# Filtering with multiple conditions
filtered_df = df[(df['Score'] > 80) & (df['Passed'] == True)]

print("FIltered Dataframe : \n", filtered_df)
```
***Output***

`Example Filtered DataFrame : `
| Name  | Score | Passed |
|-------|-------|--------|
| Alice | 85    | True   |