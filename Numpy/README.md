
## Additional Resources
[Numpy For Machine Learning & Deep Learning](https://dev.to/arju10/numpy-for-machine-learning-deep-learning-5hbb)


## Numpy
Numpy is a python library used to work with arrays and stands for Numarical python. It works on linear algebra, fourier transform, and matrices domain.
Numpy is faster than list because numpy provides array object.

## Numpy Functions:
`Note: ` To use numpy always import it.
```python
import numpy as np # Here, numpy is imported as np
```
</br>


**1. zeros():** It creates a array with zeros. Example: 
```python
array_zeros = np.zeros((3,3))
print("Array of Zeros: \n", array_zeros)
```
**Output** 

Array of Zeros: </br>
 `[[0. 0. 0.]` </br>
 `[0. 0. 0.]` </br>
 `[0. 0. 0.]]` </br>


**2. ones():** It creates a array with ones. Example: 
```python
array_ones = np.ones((2,2))
print("Array of ones: \n",array_ones)
```
**Output** 

Array of ones:  </br>
 `[[1. 1.]` </br>
 `[1. 1.]]` </br>


**3. full():** It creates a array with all elements as 7. Example: 
```python
array_full = np.full((2,2),7)
print("Array with all elements as 7 : \n",array_full)
```
**Output** 

Array with all elements as 7 : </br> 
 [[7 7] </br> 
 [7 7]]


**4. range():** It creates a array between 0 to 20. Example: 
```python
array_range = np.arange(20)
print("Array with range of numbers : ",array_range)
```
**Output** 

Array with range of numbers : 
 `[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]`

 **5. random():** </br>
 Example: 
```python
import numpy as np

# Create array
random_array = np.random.rand(3,3) # Random values in 3 X 3
normal_array = np.random.randn(3,3) # Random values with a normal distribution

print("Randmon Array : \n", random_array)
print("\n")
print("Normal Array : \n", normal_array)
```
**Output** 

Randmon Array : </br>
 `[[0.14635308 0.23362121 0.28310351]`</br>
 `[0.23209788 0.67298124 0.84145588]`</br>
 `[0.6829577  0.45439367 0.05747398]]`</br>


Normal Array : </br>
 `[[-0.57461744 -0.09078458 -0.50067585]`</br>
 `[ 0.86439072 -1.44615505  0.25666949]`</br>
 `[ 0.01952512 -1.70556208 -0.80816368]]`</br>


 **6. transpose():** </br>
 Example: 
```python
import numpy as np

# Create 2D array
original_array = np.array([
    [1,2],
    [3,4]
])

# Transpose the array
transposed_array = np.transpose(original_array)

print("Original Array: \n", original_array)
print("Transposed Array: \n", transposed_array)
```
**Output** 

Original Array: </br>
 `[[1 2]` </br>
 `[3 4]]`</br>
Transposed Array: </br>
` [[1 3]`</br>
` [2 4]]`
</br>

**7. reshape():** </br>
 Example: 
```python
import numpy as np

# Create array
original_array = np.array(
    [1,4,6,7,8,9]
)

# Reshaping to different dimensions
reshaped_array = original_array.reshape((2,3))

print("Original Array : \n", original_array)
print("\n")
print("Reshaping Array : \n", reshaped_array)
```
**Output** 

Original Array : </br>
 `[1 4 6 7 8 9]`</br></br>
Reshaping Array : </br>
 `[[1 4 6]` </br>
 `[7 8 9]]`
</br>

**8. concatenate():** </br>
 Example: 
```python
import numpy as np

# Create an array
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

# Concatenating arrays
concatenating_array = np.concatenate((array1, array2))

print("Concatenate Array : ", concatenating_array)
```
**Output** 

`Concatenate Array :  [1 2 3 4 5 6]`
</br>

**9. array_split():** </br>
 Example: 
```python
import numpy as np

# create an array
array = np.array(
    [1,2,34,4,5,6]
)

# Spliting the array into three parts
split_arrays = np.array_split(array,3)

print("Original Array : ", array)
print("Spiting Array : ", split_arrays)
```
**Output** 

`Original Array : [ 1  2 34  4  5  6]` </br>
`Spiting Array :  [array([1, 2]), array([34,  4]), array([5, 6])]`
</br>

**10. linspace():** </br>
 Example: 
```python
import numpy as np

# Generating a linear space array with evenly spaced values
linear_space = np.linspace(0,10,5)

print("Linear Space : ", linear_space)

```
**Output** 

`Linear Space :  [ 0.   2.5  5.   7.5 10. ]`
</br>

**11. meshgrid():** </br>
 Example: 
```python
import numpy as np

# Create arrays
x = np.array([1,2,3])
y = np.array([4,5,6])

# Create a meshgrid
x,y = np.meshgrid(x,y)

print("Meshgrid X : \n",x)
print("\n")
print("Meshgrid Y : \n",y)


```
**Output** 

`Meshgrid X :`  </br>
 [[1 2 3] </br>
 [1 2 3]</br>
 [1 2 3]]</br>


`Meshgrid Y : `</br>
 [[4 4 4]</br>
 [5 5 5]</br>
 [6 6 6]]</br>
</br>

**12. clip():** </br>
 Example: 
```python
import numpy as np

# Create a array
array = np.array([1,2,4,5])

# Clipping values to be between 2 and 4
clipped_array = np.clip(array, 2,4)

print("Original Array",array)
print("Clipped Array",clipped_array)
```
**Output** 

`Original Array [1 2 4 5]` </br>
`Clipped Array [2 2 4 4]`
</br>

### Arithmetic Operations
**1. add():** It adds minimum two arrays. Both array size should be same. </br> </br>
**2. subtract():** It will minus from one array to another array & Both array size should be same.</br> </br>
**3. multiply():** It multiplys between minimum two arrays. Both array size should be same.</br> </br>
**4. divide():** It divides  an array with another array & Both array size should be same.</br> </br>
Examples:
```python
import numpy as np

# Create arrays
array1 = np.array([10,20,30])
array2 = np.array([40,50,60])

# Arithmetic Operations
added = np.add(array1, array2)
subtracted = np.subtract(array1 , array2)
multiplied = np.multiply(array1, array2)
divided = np.divide(array1, array2)

print("Added: ", added)
print("Subtracted :", subtracted)
print("Multiplied: ", multiplied)
print("Divided: ", divided)
```
**Output** 

Added:  [50 70 90] </br>
Subtracted : [-30 -30 -30]  </br>
Multiplied:  [ 400 1000 1800] </br>
Divided:  [0.25 0.4  0.5 ] </br>

**5. power():** A power is a number multiplied by itself a certain number of times, represented by an exponent. For example:
 **10^2** means 10 multiplied by itself, which is \(10 X 10 = 100\). </br> </br>
**6. sqrt():** A square root of a number is a value that, when multiplied by itself, gives the original number. It is represented by the square root symbol (√).

For example:

- √121 = 11

In this case, 11 × 11 = 121, so the square root of 121 is 11.

### Properties of Square Roots

1. The square root of a positive number has both a positive and a negative solution (e.g., √25 = ±5), but typically, the positive root is used.
2. The square root of 0 is 0.
3. Negative numbers do not have real square roots (they result in imaginary numbers).

Examples :

- √144 = 12
- √64 = 8
- √49 = 7

```python
import numpy as np

# Create array
array = np.array([2,6,4,3,7])

# Power & Square Root
squared = np.power(array, 2)
sqrt = np.sqrt(array)

print("Squared Array :", squared)
print("Square root of array :", sqrt)
```
**Output** 

Squared Array :` [ 4 36 16  9 49]` </br>
Square root of array : `[1.41421356` `2.44948974` `2.`         `1.73205081 2.64575131] `
</br> </br>

### Trigometric Functions
**1. sin():**  </br> </br>
**2. cos():**  </br> </br>
**3. tan():**  </br> </br>

Example: 
```python
import numpy as np

# Create array
angles = np.array([0, np.pi/2, np.pi])

# Trigometric functions
sin_array = np.sin(angles)
cos_array = np.cos(angles)
tan_arraY = np.tan(angles)


print("Sins of angles: ", sin_array)
print("Cos of angles : ", angles)
print("Tan of angles : ", angles)
```
**Output** 

Sins of angles:  `[0.0000000e+00 1.0000000e+00 1.2246468e-16]` </br>
Cos of angles : ` [0.         1.57079633 3.14159265]` </br>
Tan of angles : ` [0.         1.57079633 3.14159265]` </br>
</br>
</br>

### Exponential & Logarithm Function
**1. exp():**  </br> </br>
**2. log():**  </br> </br>
Example: 
```python
import numpy as np

# Create an array
array = np.array([10,20,30])

# Exponential & Logarithm functions
exp_array = np.exp(array)
log_array = np.log(array)

print("Exponential of Array: ",exp_array)
print("Logarithm of Array: ",log_array)
```

**Output** </br>
Exponential of Array:  `[2.20264658e+04 4.85165195e+08 1.06864746e+13]`
</br>
Logarithm of Array:  `[2.30258509 2.99573227 3.40119738]`
</br>

### Statistical Functions

**1. mean():**  </br> </br>
**2. median():**  </br> </br>
**3. std():**  </br> </br>
**4. var():**  </br> </br>

```python
import numpy as np

# Create array
array = np.array(
    [1,2,3,4,5]
)

# Calculating statistical functions
mean = np.mean(array)
median = np.median(array)
std_dev = np.std(array)
variance = np.var(array)

print("Mean  : ", mean)
print("Median : ", median)
print("Standard deviation : ", std_dev)
print("Variance : ", variance)
```
**Output** </br>
Mean  :  `3.0`</br>
Median :  `3.0`</br>
Standard deviation :  `1.4142135623730951`</br>
Variance :  `2.0`
</br>
</br>

### Unique Elements and Their Counts

**1. unique():** It finds the unique elements from array. If pass the parameter`retuen_counts = True`, it will show the number of unique elements from an array. </br> </br>

Example: 

```python
import numpy as np

# Create an array
array = np.array(
    [14,1,54,5,125,214,1,2,43,4,2,2,41,14,54,214,1]
)

# Finding Unique Element and their counts
unique_element , counts= np.unique(array, return_counts=True)

print("Unique Elements : ", unique_element)
print("Counts of Unique Elements: ", counts)
```
**Output** </br>
Unique Elements :  `[  1   2   4   5  14  41  43  54 125 214]` </br>
Counts of Unique Elements:  `[3 3 1 1 2 1 1 2 1 2]`
</br>

### Cumulative Sum and Product
**1. cumsum():** </br>
**2. cumprod():** </br>
 Example: 
```python
import numpy as np

# Create a array
array = np.array([1,2,4,5])

# Calculating cumulative sum and product
cumulative_sum = np.cumsum(array)
cumulative_product = np.cumsum(array)

print("cumulative sum : ", cumulative_sum)
print("cumulative product : ", cumulative_product)
```

**Output** 

`cumulative sum :  [ 1  3  7 12] `</br>
`cumulative product :  [ 1  3  7 12]`
</br>

### Broadcasting
Adding a scaler to an array.</br>
Example:
```python
import numpy as np

# create array
array = np.array(
    [1,2,3]
)

# Braodcasting: Adding a scaler to an array
result = array + 10

print("Original Array: ", array)
print("Array after broadcasting : ", result)
```
**Output** </br>
`Original Array:  [1 2 3]` </br>
`Array after broadcasting :  [11 12 13]`
</br>

### Sorting Array `sort()`
**1. sort():** It sorts the array by default ascending order.
```python
import numpy as np

# Create array
array = np.array(
    [2,4,5,3,10,7,8]
)

# Sort the array
sorted_array = np.sort(array,)

print("Sorted Arrays: ", sorted_array)
```
**Output** </br>
Sorted Arrays:  [ 2  3  4  5  7  8 10]
</br>


### Array Indexing & Slicing: `[row:column]` 
####  Basic Indexing and Slicing

```python
import numpy as np

# Create a array
array = np.array([1,2,4,5])

# Aceesing element by index
first_element = array[0]
last_element = array[-1]

# Slicing the array
slice_array = array[1:4]

# Selecting Specific indices
selected_elements = array[[1,3]]

# Slicing with a step
step_slice = array[::2] # Every Second Element

#Modifying values specific indices
array[[1,3]] = [100, 200]


print("First Element: ", first_element)
print("Last Element: ", last_element)
print("Sliced Element: ", slice_array)
print("Selected Elements :", selected_elements)
print("Sliced Array with Step 2 :", step_slice)
print("Modified Array : ",array)
```

**Output** </br>

`First Element:  1` </br>
`Last Element:  5` </br>
`Sliced Element:  [2 4 5] `</br>
`Selected Elements : [2 5]` </br>
`Sliced Array with Step 2 : [1 4]` </br>
`Modified Array :  [  1 100   4 200]`</br>
</br>

#### 2D Array indexing & Slicing
```python
import numpy as np

# Create a 2D array
array_2d = np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)

# Accessing individual elements
element = array_2d[1,2] # Accessing element at row 1, column 2

# Slicing Row
row_slice = array_2d[0, : ] # First row

# Slicing Column
column_slice = array_2d[:, 1] # Second Column

# Using arrays for indexing
rows = np.array([0,1,2]) 
cols = np.array([2,1,0])
indexed_elements = array_2d[rows, cols]

# Multi Dimensional Slicing
sub_array = array_2d[1:, 1:3]

print("Element at (1,2) : ", element)
print("First Row : ", row_slice)
print("Second Column: ", column_slice)
print("Indexed Elements : ", indexed_elements)
print("Sub Array (Slicing Rows & Columns) : \n", sub_array)
```

**Output** </br>
`Element at (1,2) :`  `6`
</br>
`First Row :  [1 2 3]`
</br>
`Second Column:  [2 5 8]`
</br>
`Indexed Elements :  [3 5 7]` </br>
`Sub Array (Slicing Rows & Columns) :`</br>
 [[5 6] </br>
 [8 9]]


#### 3D Array Indexing & Slicing
```python
import numpy as np

# Create a 3D array
array_3d = np.array(
    [
        [
            [10,20], [30,40]
        ],
        [
            [50,60], [70,80]
        ]
    ]
)

# Accessing elements in a 3D Array
element = array_3d[1,0,1] # Accessing element at [1, 0 , 1]

# Slicing in 3D
slice_3D = array_3d[:, 0, : ] # First row

print("Element at (1,0,1): ", element)
print("\n")
print("Sliced 3D Array : \n", slice_3D)
```

**Output** </br>
`Element at (1,0,1):  60` </br>
`Sliced 3D Array :` </br>
 [[10 20] </br>
 [50 60]]
</br>
</br>

#### Boolean Indexing
```python
import numpy as np

# Create a array
array = np.array(
    [10,20,30,40,60,80]
)

# Boolean Indexing
greater_than_20 = array[array > 20]

print("Elements greater than 20 : ",greater_than_20)
```
**Output** </br>
`Elements greater than 20 :  [30 40 60 80]`
</br>
</br>

#### Conditional Indexing
```python
import numpy as np

# Create a array
array = np.array(
    [1,2,3,4,5,6]
)

# Setting elements that satisfying a condition
array[array % 2 == 0] = -1 # Set even numbers to -1

print("Array after conditional indexing : ",array)
```
**Output** </br>
`Array after conditional indexing :  [ 1 -1  3 -1  5 -1]`
</br>
</br>