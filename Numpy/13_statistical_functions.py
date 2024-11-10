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