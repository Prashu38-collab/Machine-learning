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

# 24. Extract numbers from an array

arr = np.arange(15)
mask1=arr[(arr>=5) & (arr<=10)]

print(mask1)

a=np.random.rand(3,2)
print(a)

# 25. Sorting a NumPy array based on a specific column
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])
result=sampleArray[:,1].argsort()
sorted_Array=sampleArray[result]
print(sorted_Array)
print("Original array:")
print(sampleArray)

# 26. Delete and Insert a Column in a NumPy Array
newColumn=[1,2,3]
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
result=np.delete(sampleArray,1,axis=1)
print(result)
resultArray = np.insert(result, 1, newColumn, axis=1)
print(resultArray)

# 27. Swap column 1 and 2 in a 2D array fancy indexing
rr = np.arange(9).reshape(3, 3)
print(rr)
rr[:,[1,2]]=rr[:,[2,1]]
print(rr)

# 28.  Generate 10 random integers between 1 and 100
a=np.random.randint(1,101,10)
print(a)


#29.  Create a 3×3 array of random integers and sort it row-wise

res=np.random.randint(1,30,size=(3,3))
result=np.sort(res,axis=1)
print(result)

# 30. Shuffle an array randomly
arr = np.arange(10)
print("Original: ",arr)
np.random.shuffle(arr)
print(arr)

# 31. Create a 5×5 2D array with 1s on the border and 0s inside.

arr=np.ones(25).reshape(5,5)

mask=arr[1:4,1:4]=0
print(arr)

# 32. Check if an array contains any NaN values.
a = np.array([1, 2, np.nan, 4, 5])
print(np.isnan(a).any())

# 33. Sort the rows of a 2D array based on the values of the second column

arr = np.array([[8, 4, 1],
                [5, 2, 7],
                [6, 9, 3]])
res=arr[:,1].argsort()
sorted_Arr=arr[res]
print(sorted_Arr)

# 34. Flatten a multi-dimensional NumPy array

arr = np.array([[1, 2], [3, 4], [5, 6]])
r=np.ravel(arr)
print(r)

# 35. Stack two arrays vertically and horizontally
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
hstack=np.hstack((a,b))
print(hstack)
vstack=np.vstack((a,b))
print(vstack)

# 36. Split an array into 3 equal parts
arr = np.arange(9)
result=np.split(arr,3)
print(result)

# 37. Perform Addition and Squaring on Arrays
arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])
result=arrayOne+arrayTwo
print(result**2)


# 38. Invert a matrix
arr = np.array([[1, 2], [3, 4]])
result=np.linalg.inv(arr)
print(result)

# 39. Use boolean indexing to filter values less than a given number

arr = np.array([5, 12, 29, 30, 44, 7, 18])
mask=arr[arr<30]
print(mask)

# 40. Count the number of occurrences of each unique element
arr = np.array([2, 3, 2, 5, 3, 3, 2, 5])
result,counts=np.unique(arr,return_counts=True)
for v, c in zip(result, counts):
    print(f"Value {v} occurs {c} time(s)")


# 41. Find the intersection and union of two arrays
a = np.array([1, 2, 3, 5, 7])
b = np.array([3, 4, 5, 6, 7])
result=np.intersect1d(a,b)
result1=np.union1d(a,b)
print(result1)


# 42.  Transpose a matrix

arr = np.array([[1, 2], [3, 4]])
r=np.transpose(arr)
print(r)

# 43. Compute the eigenvalues and eigenvectors of a matrix

A = np.array([[4, 2],
              [1, 3]])

eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:\n", eigvals)
print("Eigenvectors (columns):\n", eigvecs)

# 44. Solve a linear equation x + 2y = 8 and 3x + 4y = 18.

A = np.array([[1, 2], [3, 4]])
b = np.array([8, 18])
solution = np.linalg.solve(A, b)
print(solution)

# 45. Create an 8×8 checkerboard pattern using 0s and 1s

a=np.zeros(64).reshape(8,8)
a[1::2,::2]=1
a[::2,1::2]=1
print(a)

