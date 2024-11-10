
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

### Create Numpy array


**1. zeros():** It creates a array with zeros. Example: 
```python
array_zeros = np.zeros((3,3))
print("Array of Zeros: \n", array_zeros)
```
**Output** 

Array of Zeros: </br>
 [[0. 0. 0.] </br>
 [0. 0. 0.] </br>
 [0. 0. 0.]] </br>


**2. ones():** It creates a array with ones. Example: 
```python
array_ones = np.ones((2,2))
print("Array of ones: \n",array_ones)
```
**Output** 

Array of ones:  </br>
 [[1. 1.] </br>
 [1. 1.]] </br>


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
 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

 **6. random():** </br>
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
 [[0.14635308 0.23362121 0.28310351]</br>
 [0.23209788 0.67298124 0.84145588]</br>
 [0.6829577  0.45439367 0.05747398]]</br>


Normal Array : </br>
 [[-0.57461744 -0.09078458 -0.50067585]</br>
 [ 0.86439072 -1.44615505  0.25666949]</br>
 [ 0.01952512 -1.70556208 -0.80816368]]</br>


 **5. transpose():** </br>
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
 [[1 2] </br>
 [3 4]]</br>
Transposed Array: </br>
 [[1 3]</br>
 [2 4]]
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

Squared Array : [ 4 36 16  9 49] </br>
Square root of array : [1.41421356 2.44948974 2.         1.73205081 2.64575131] 
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

Sins of angles:  [0.0000000e+00 1.0000000e+00 1.2246468e-16] </br>
Cos of angles :  [0.         1.57079633 3.14159265] </br>
Tan of angles :  [0.         1.57079633 3.14159265] </br>
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
Exponential of Array:  [2.20264658e+04 4.85165195e+08 1.06864746e+13]
</br>
Logarithm of Array:  [2.30258509 2.99573227 3.40119738]
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
Original Array:  [1 2 3] </br>
Array after broadcasting :  [11 12 13]
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


### Array Indexing `[row:column]`
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
```

**1. Accessing Individual elements:** 
```python
# Accessing individual elements
element = array_2d[1,2] # Accessing element at row 1, column 2

print("Element at (1,2) : ", element)
```
**Output** </br>
Element at (1,2) :  6
</br>

**2. Slicing Row:** 
```python
row_slice = array_2d[0, : ] # First row
print("First Row : ", row_slice)
```

**Output** </br>
First Row :  [1 2 3]
</br>

**3. Slicing Column:** 
```python
column_slice = array_2d[:, 1] # Second Column
print("Second Column: ", column_slice)
```

**Output** </br>
Second Column:  [2 5 8]
</br>

### Boolean Indexing
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
Elements greater than 20 :  [30 40 60 80]
</br>
</br>
