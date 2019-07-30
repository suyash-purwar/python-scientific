import numpy as np

arr = np.array([120, 37, 91, 27, 35])
matrix = np.array([(1.6, 4.1, 2), (22, 10, 21)])

''' array.ndim prints the dimension of the array '''
print(arr.ndim)
print(matrix.ndim)

''' array.shape prints the number of rows and columns
    in the form of (n, m) tuple '''
print(arr.shape)
print(matrix.shape)

''' array.size prints the total number of elements in a n-dim matrix.
    This is equal to the product of elements obtained from array.shape '''
print(arr.size)
print(matrix.size)

''' array.dtype prints the type of array '''
print(arr.dtype)
print(matrix.dtype)

''' array.itemsize prints the size occupied by a single element
    of an n-dimensional array '''
print(arr.itemsize)
print(matrix.itemsize)

''' np.arange(*start, end, step) function similar to range() in python '''
print(np.arange(15))

''' array.reshape(n, m) transforms the number of rows and columns in
    an n-dimensional array '''
array_two = np.arange(0, 30)
matrix2 = array_two.reshape(2, 3, 5)
matrix3 = array_two.reshape(10, 3)
print(matrix3)
print(matrix2)