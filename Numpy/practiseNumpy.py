#  1. Create a 1D NumPy array of numbers from 0 to 9
import numpy as np 
# this converts list to a numpy array
array=np.array([0,1,2,3,4,5,6,7,8,9])
print(array)
print(type(array))

# 2. Convert 1D array to 2D
# we use reshape to convert 1D to 2D
arr=np.arange(1,7)
print(arr)

arr_2d= arr.reshape(2,3)
print(arr_2d)

# 3. Print array attributes

my_array = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.uint8)

print(f"The shape of an array is {my_array.shape}.")
print(f"The number of dimensions is {my_array.ndim}")
print(f"The size of each element in bytes is {my_array.itemsize}")

# 4. Create a 3×3 NumPy array of all True
# np.ones= 
arr=np.ones((3,3),dtype=bool)
print(arr)

# 5. Create a 1D array filled with zeros and another filled with ones

arr=np.zeros((6))
arr1=np.ones((6))

print(arr1)
print(arr)

# 6. Create a 1D array of 10 evenly spaced values between 5 and 50

