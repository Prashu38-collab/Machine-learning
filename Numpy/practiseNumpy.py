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
arr=np.arange(5,51,5)
print(arr)
# or i can do this particularly as 
arr=np.linspace(5,50,10)
print(arr)

# 7. Convert a Python list into a NumPy array

arr=np.array([1,2,4,5])
print(arr)

# 8.  Find the memory size of a NumPy array of numbers from 0 to 9

arr=arr=np.array([1,2,3,4,9,5,6,7,8,0],dtype=np.uint64) #bydefualt its unit=64
print(arr.nbytes)

# 9. Reverse a 1D NumPy array

arr = np.arange(10)
reverse=arr[::-1]
print(reverse)

# 10. Create a 3×3 identity matrix
arr=np.eye((3))
print(arr)

# 11. Create a 4×4 array and extract its first row and last column

matrix = np.arange(16).reshape(4, 4)
print(matrix)

print("First Row:", matrix[1:2])
print("Last Column: ", matrix[:,-1])

# 12. Extract Odd Rows and Even Columns

sampleArray = np.array([
    [3, 6, 9, 12], 
    [15, 18, 21, 24], 
    [27, 30, 33, 36], 
    [39, 42, 45, 48], 
    [51, 54, 57, 60]
])


print(sampleArray[1:4:2,0:3:2])

# 13. Stack arrays horizontally
a = np.array([1, 2, 3]) 
b = np.array([4, 5, 6])

arr=np.hstack((a,b))
print(arr)

# 14. Slice the first two rows and first two columns from a 4×4 array

array=np.array([
 [ 1 , 2 , 3 , 4],
 [ 5 , 6 , 7 , 8],
 [ 9, 10, 11, 12],
 [13, 14 ,15 ,16]
 ])
print(array[0:2,0:2])

# 15. Replace all odd numbers in a NumPy array with -1
original=np.array([ 1 , 2 , 3 , 4 , 5,  6  ,7  ,8  ,9, 10])
original[original%2!=0]=-1
print(original)

# 16. Get the indices of non-zero elements in an array
arr = np.array([1, 0, 2, 0, 3, 0, 4])
print(np.nonzero(arr))

# 17. Find the common items between two arrays
a = np.array([1, 2, 3, 2, 8, 4, 2, 4])
b = np.array([2, 4, 5, 6, 8])
print(np.intersect1d(a,b))

# 18. Perform arithmetic operations on two NumPy arrays element-wise
# Add two NumPy arrays element by element.
# Multiply two NumPy arrays element by element.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])


result=np.add(a,b)
result1=np.multiply(a,b)
print(result1)

# 19. Matrix multiplication
# Write a code to compute the dot product of two NumPy arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result=np.dot(a,b)
print(result)

# 20. Compute the mean, median, and standard deviation of a NumPy array
arr = np.array([10, 20, 30, 100, 200, 300])

print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))

# 21. Remove common items from array
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
mask=np.setdiff1d(a,b)
print(mask)


# 22. Normalize a NumPy array (values between 0 and 1)

arr = np.array([10, 20, 30, 40, 50])
# Min-Max Normalization formula
normalized_arr = (arr - arr.min()) / (arr.max() - arr.min())
print(normalized_arr)

# 23. Get the positions where elements of array a and b match
a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 4, 3, 7, 8])
result=np.where(a==b)
print(result)