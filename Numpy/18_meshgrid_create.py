import numpy as np

# Create arrays
x = np.array([1,2,3])
y = np.array([4,5,6])

# Create a meshgrid
x,y = np.meshgrid(x,y)

print("Meshgrid X : \n",x)
print("\n")
print("Meshgrid Y : \n",y)
