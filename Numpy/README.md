
## Additional Resources
[Numpy For Machine Learning & Deep Learning](https://dev.to/arju10/numpy-for-machine-learning-deep-learning-5hbb)


## Numpy
Numpy is a python library used to work with arrays and stands for Numarical python. It works on linear algebra, fourier transform, and matrices domain.
Numpy is faster than list because numpy provides array object.

## Numpy Functions:
`Note: ` To use numpy always import it.
```
import numpy as np // Here, numpy is imported as np
```
</br>

### Create Numpy array


**1. zeros():** It creates a array with zeros. Example: 
```
array_zeros = np.zeros((3,3))
print("Array of Zeros: \n", array_zeros)
```
**Output** 

Array of Zeros: </br>
 [[0. 0. 0.] </br>
 [0. 0. 0.] </br>
 [0. 0. 0.]] </br>


**2. ones():** It creates a array with ones. Example: 
```
array_ones = np.ones((2,2))
print("Array of ones: \n",array_ones)
```
**Output** 

Array of ones:  </br>
 [[1. 1.] </br>
 [1. 1.]] </br>


**3. full():** It creates a array with all elements as 7. Example: 
```
array_full = np.full((2,2),7)
print("Array with all elements as 7 : \n",array_full)
```
**Output** 

Array with all elements as 7 : </br> 
 [[7 7] </br> 
 [7 7]]


**4. range():** It creates a array between 0 to 20. Example: 
```
array_range = np.arange(20)
print("Array with range of numbers : ",array_range)
```
**Output** 

Array with range of numbers : 
 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

</br>

</br>

### Arithmetic Operations
**1. add():** It adds minimum two arrays. Both array size should be same. </br>
**2. subtract():** It will minus from one array to another array & Both array size should be same.</br>
**3. multiply():** It multiplys between minimum two arrays. Both array size should be same.</br>
**4. divide():** It divides  an array with another array & Both array size should be same.</br>
Examples:
```
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



### Array Indexing `[row:column]`
```
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
```
# Accessing individual elements
element = array_2d[1,2] # Accessing element at row 1, column 2

print("Element at (1,2) : ", element)
```
**Output** </br>
Element at (1,2) :  6
</br>

**2. Slicing Row:** 
```
row_slice = array_2d[0, : ] # First row
print("First Row : ", row_slice)
```

**Output** </br>
First Row :  [1 2 3]
</br>

**3. Slicing Column:** 
```
column_slice = array_2d[:, 1] # Second Column
print("Second Column: ", column_slice)
```

**Output** </br>
Second Column:  [2 5 8]
</br>

### Boolean Indexing
```
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

### Exponential & Logarithm Function
```
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