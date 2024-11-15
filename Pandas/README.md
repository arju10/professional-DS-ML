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

### Creating Custom Categorical Data
```python
import pandas as pd

# Create dataframe
data = {'Name':['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85, 70, 95,60]}
df = pd.DataFrame(data)

# Creating a new column with categorical data
df['Performance'] = pd.cut(df['Score'], bins=[0,70,90,100], labels=['Poor', 'Average', 'Excellent'])

print('Dataframe with categorical performance : \n', df)
```
***Output***
`DataFrame with Categorical Performance : `

| Name    | Score | Performance |
|---------|-------|-------------|
| Alice   | 85    | Average     |
| Bob     | 70    | Poor        |
| Charlie | 95    | Excellent   |
| David   | 60    | Poor        |

### Rolling Window Calculations
```python
import pandas as pd

# Create a time series dataframe
data_range = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = {'Sales': [100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}
df = pd.DataFrame(data, index= data_range)

# Calculating a rolling mean with a window of 3 days
df['Rolling Mean'] = df['Sales'].rolling(window=3).mean()

print("Dataframe with rolling mean : \n", df)
```
***Output***
`DataFrame with Rolling Mean : ` </br>

| Date       | Sales | Rolling Mean |
|------------|-------|--------------|
| 2023-01-01 | 100   | NaN          |
| 2023-01-02 | 200   | NaN          |
| 2023-01-03 | 150   | 150.000000   |
| 2023-01-04 | 300   | 216.666667   |
| 2023-01-05 | 250   | 233.333333   |
| 2023-01-06 | 400   | 316.666667   |
| 2023-01-07 | 300   | 316.666667   |
| 2023-01-08 | 350   | 350.000000   |
| 2023-01-09 | 300   | 316.666667   |
| 2023-01-10 | 400   | 350.000000   |

### Shift and Lagging Data
```python
import pandas as pd

# Create Dataframe
data = {'Date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
        'Temperature': [30, 32, 35,33, 31]}

df = pd.DataFrame(data)

# Shifting data by one to create a lag
df['Prev Day Temp'] = df['Temperature'].shift(1)

print('Dataframe with shifted data: \n', df)
```
***Output***
`DataFrame with Previous Day Temperature:`

| Date       | Temperature | Prev Day Temp |
|------------|-------------|---------------|
| 2023-01-01 | 30          | NaN           |
| 2023-01-02 | 32          | 30.0          |
| 2023-01-03 | 35          | 32.0          |
| 2023-01-04 | 33          | 35.0          |
| 2023-01-05 | 31          | 33.0          |

### Cumulative sum and product
```python
import pandas as pd

# Create dataframe
data = {'Sales': [100, 200, 150, 300, 250]}
df = pd.DataFrame(data)

# Calculating cumulative sum and product
df['cumulative sum'] = df['Sales'].cumsum()
df['cumulative product'] = df['Sales'].cumprod()

print('DataFrame with cumulative operations:\n', df)
```
***Output***
`DataFrame with Cumulative Operations:`

| Sales | Cumulative Sum | Cumulative Product |
|-------|-----------------|--------------------|
| 100   | 100             | 100                |
| 200   | 300             | 20000              |
| 150   | 450             | 3000000            |
| 300   | 750             | 900000000          |
| 250   | 1000            | 225000000000      |

### Merging on multiple columns
```python
import pandas as pd

# Create two dataframe
df1 = pd.DataFrame({'ID':[1,2,3], 'Year':[2020,2021,2023], 'Name':['Alice','Bob','Charlie'] })
df2 = pd.DataFrame({'ID':[2,3,1], 'Year':[2023,2023,2020], 'Score':[88,92,75]})

# Merging on multiple columns
merged_df = pd.merge(df1,df2, on=['ID','Year'], how='inner')

print('Merged Dataframe on multiple columns : \n', merged_df)
```
***Output***
`Merged DataFrame on Multiple Columns:`

| ID | Year | Name    | Score |
|----|------|---------|-------|
| 1  | 2020 | Alice   | 75    |
| 3  | 2023 | Charlie | 92    |

### Handling Outliers
```python
import pandas as pd

# Create dataframe
data = {'Value': [10, 12, 14, 100, 15, 13, 12]}
df = pd.DataFrame(data)

# Indentifying outliers using the IQR method
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Value'] < (Q1 - 1.5 * IQR)) | (df['Value'] > (Q3 + 1.5 * IQR))]

print('Outliers: \n', outliers)
```
***Output***
`DataFrame with Outliers:`

| Value |
|-------|
| 10    |
| 15    |
| 20    |
| 100   |

Here, the value `100` is an outlier compared to the other values.

### Creating a pivot table with multiple aggregation
```python
import pandas as pd

# Create dataframe
data = {'City':['NY', 'LA', 'NY','SF','LA'], 'Year':[2020,2020,2021,2021,2020], 'Sales':[100, 150, 200, 250,300]}
df = pd.DataFrame(data)

# Create a pivot table with multiple aggregation
pivot_table = pd.pivot_table(df, values='Sales', index='City', columns='Year', aggfunc=['sum', 'mean'])

print('Pivot table with multiple aggregation: \n', pivot_table)
```
***Output***
`Pivot Table with Multiple Aggregation : `

| City | Year  | Sum   | Mean  |
|------|-------|-------|-------|
| LA   | 2020  | 450.0 | 225.0 |
| NY   | 2020  | 100.0 | 100.0 |
| NY   | 2021  | 200.0 | 200.0 |
| SF   | 2021  | 250.0 | 250.0 |

Here, a pivot table is created with `sum` and `mean` as the aggregation functions.

### Using `map()` for Value Replacement
```python
import pandas as pd

# Create dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Department':['HR', 'IT', 'Finance']}
df = pd.DataFrame(data)

# Mapping department to codes
department_map = {'HR':1, 'IT':2, 'Finance':3}
df['Dept Code'] = df['Department'].map(department_map)

print("Dataframe with mapped values: \n", df)
```
***Output***
`DataFrame with Mapped Values: `

| Name    | Department | Dept Code |
|---------|------------|-----------|
| Alice   | HR         | 1         |
| Bob     | IT         | 2         |
| Charlie | Finance    | 3         |

Here, the department names are mapped to department codes.

### Detecting Duplicates
```python
iimport pandas as pd

# Create a dataframe with duplicate rows
data = {'ID':[1,2,2,3,4,4], 'Value': [10, 20,20,30,40,40]}
df = pd.DataFrame(data)

# Detecting duplicates
duplicates = df[df.duplicated()]

print('Duplicate Row : \n', duplicates)
```
***Output***
`DataFrame with Duplicate Rows:`    

| ID  | Value |
|-----|-------|
| 2   | 20    |
| 4   | 40    |
| 2   | 20    |
| 4   | 40    |

In this example, the rows with ID `2` and `4` are duplicates.

### Using `explode()` for list in columns
```python
import pandas as pd

# Create a dataframe with lists in a column
data = {'ID':[1,2], 'Hobbies':[['Reading', 'Swimming'], ['Running', 'Cycling'] ]}
df = pd.DataFrame(data)

# Explodeing the 'Hobbies' Column
exploded_df = df.explode('Hobbies')

print("Dataframe after exploring lists: \n", exploded_df)
```
***Output***
`DataFrame After Exploring Lists:`

| ID | Hobbies   |
|----|-----------|
| 1  | Reading   |
| 1  | Swimming  |
| 2  | Running   |
| 2  | Cycling   |

In this example, each `hobby` in a list associated with an ID is expanded into its own row.


### Using `rank()` to rank values
```python
import pandas as pd

# Create dataframe
data = {'Name' : ['Alice', 'Bob', 'Charlie', 'David'], 'Score': [85,90,78,92]}
df = pd.DataFrame(data)

# Ranking scores in descending order
df['Rank'] = df['Score'].rank(ascending=False)

print('Dataframe with ranked scores : \n', df)
```
***Output***
`DataFrame with Ranked Scores:`

| Name    | Score | Rank |
|---------|-------|------|
| Alice   | 85    | 3.0  |
| Bob     | 90    | 2.0  |
| Charlie | 78    | 4.0  |
| David   | 92    | 1.0  |

In this example, the `scores` are ranked in descending order, with the highest score receiving the highest rank.

### Using `applymap()` for element-wise operations
```python
import pandas as pd

# Create dataframe
data = {'A': [1,2,3], 'B':[4,5,6]}
df = pd.DataFrame(data)

# Applying an operation to each element in the Dataframe
df_transformed = df.applymap(lambda x:x**2)

print("Dataframe with squared values : \n", df_transformed)
```
***Output***
`DataFrame with Ranked Scores: `

| Name    | Score | Rank |
|---------|-------|------|
| Alice   | 85    | 3.0  |
| Bob     | 90    | 2.0  |
| Charlie | 78    | 4.0  |
| David   | 92    | 1.0  |

In this example, the `scores` are ranked in `descending` order, with the highest score receiving the highest rank.
