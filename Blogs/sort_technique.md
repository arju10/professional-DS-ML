## List:
 
A list is a collection of items in python, created using square brackets [] . List can contain different data types, including numbers, strings and other lists. List is mutable ( It can't changed/modified).

## Sort:

In list very easily numbers can be sorted.

## Prerequisites for Sorting a List of Numbers:

Before starting sort the list, you need to know about List & How to create a list.

### Create a List:
In the beginning, We will create a list

```
# Create a list with Numbers
my_list = [10,80,20,60,30,40,70]

# Print the list
print("List: ", my_list)
```
Here, `10`, `80`, `20`, `60`, `30`, `40` and `70` are Numbers or we can call integer type data.
We will store these numbers in `my_list` variable. 
`print()` is a builtin function in python which used to print or show the result whatever we want.

---

## Multiple Ways to Sort List of Numbers or Integers
There  are many ways sort a list, here I talk about some technique which are used for sort a list.

### Method 1: Using the builtin sorted() function
sorted() is a builtin methods in python.By default, It sorted the number in ascending order. But If you want to descending the number just put , `reverse=True` parameter for descending the numbers.

**- Ascending order:**

```
# Create a list 
numbers_list = [10,80,20,60,30,40,70]

# Sorting in ascending order using sorted()
sorted_num_ascending = sorted(numbers_list)

# Displaying the ascending sorted numbers
print(sorted_num_ascending)
```

**Output:** `[10, 20, 30, 40, 60, 70, 80]`

**- Descending Order:**
```
# Create a list 
numbers_list = [10,80,20,60,30,40,70]

# Sorting in descending order using sorted() and add paremeter reverse = true
sorted_num_descending = sorted(numbers_list,  reverse=True)

# Displaying the descending sorted numbers
print(sorted_num_descending)
```
Output: `[80, 70, 60, 40, 30, 20, 10]`

### Method 2: Using the builtin sort() function
sort() is a builtin methods in python.By default, It sorted the number in ascending order. But If you want to descending the number just put , `reverse=True` parameter for descending the numbers.
`Note:` It is same as sorted() function.but a difference between them;
- sort() function change the original list , while sorted() method keep the original list , and store the sorted list in a new variable.

**- Ascending order:**

```
# Create a list 
numbers_list = [10,80,20,60,30,40,70]

# Sorting in ascending order using sort() 
numbers_list.sort()

# Displaying the ascending sorted numbers
print(numbers_list)
```

**Output:** `[10, 20, 30, 40, 60, 70, 80]`

**- Descending Order:**
```
# Create a list 
numbers_list = [10,80,20,60,30,40,70]

# Sorting in descending order using sort() and add paremeter reverse = True
numbers_list.sort(reverse=True)

# Displaying the descending sorted numbers
print(numbers_list)
```
Output: `[80, 70, 60, 40, 30, 20, 10]`

### Method 3: Using Lambda function with sorted()

If there is need any complex criteria for sorting, lambda function can be used there.
For example:
```
# Create a list 
numbers_list =[25, 17, 23, 51, 50]

# Sorting by remainder when divided by 5 using lambda function with sorted()
sorted_num_remainder = sorted(numbers_list, key=lambda x: x % 5)

# Displaying the sorted numbers
print(sorted_num_remainder)
```
Output: `[25, 50, 51, 17, 23]`

### Method 4: Using slicing technique `[::-1]`

Elements of a list can be reverse using slicing technique.In slicing, there are no direct method to sort a list, but can reverse a list.

```
# Create a list 
numbers_list = [10,80,20,60,30,40,70]

# Reversing the list using slicing
reversed_number = numbers_list[::-1]

# Displaying the reversed numbers
print(reversed_number)
```
Output: `[70, 40, 30, 60, 20, 80, 10]`

### Method 5: Using heapq module for large lists
If there is need any deep complex criteria for sorting, heapq can be used there.heapq is heap based algorithm which is very efficient memory rather than other sorting methods.
For example:

```
import heapq as hq
# Create a list 
numbers_list =[25, 17, 23, 51, 50]

# Sorting in descending order using heapq
hq.heapify(numbers_list)
sorted_num_hq = [hq.heappop(numbers_list) for _ in range(len(numbers_list))]

# Displaying the sorted numbers
print(sorted_num_hq)
```
Output: `[17, 23, 25, 50, 51]`

