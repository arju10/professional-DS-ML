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
