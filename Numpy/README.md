# Numpy
Numpy is a python library used to work with arrays and stands for Numarical python. It works on linear algebra, fourier transform, and matrices domain.
Numpy is faster than list because numpy provides array object.

## Numpy Functions:

**1. zeros():** It creates a array with zeros. Example: 
```
array_zeros = np.zeros((3,3))
print("Array of Zeros: \n", array_zeros)
```
`Output` 
```
Array of Zeros: 
 [[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]
```

**2. ones():** It creates a array with ones. Example: 
```
array_ones = np.ones((2,2))
print("Array of ones: \n",array_ones)
```
`Output` 
```
Array of ones: 
 [[1. 1.]
 [1. 1.]]
```

**3. full():** It creates a array with all elements as 7. Example: 
```
array_full = np.full((2,2),7)
print("Array with all elements as 7 : \n",array_full)
```
`Output` 
```
Array with all elements as 7 : 
 [[7 7]
 [7 7]]
```

**4. range():** It creates a array between 0 to 20. Example: 
```
array_range = np.arange(20)
print("Array with range of numbers :\n",array_range)
```
`Output` 
```
Array with range of numbers :
 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
```