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

