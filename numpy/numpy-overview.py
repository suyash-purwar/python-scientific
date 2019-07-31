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

''' The type of the array can also be specified at the time of creation '''
float_arr = np.array([(4, 2.3), (23, 12), (98, 76)], dtype=np.float64)
complex_arr = np.array([(4, 2, 5), (3, 1, 9)], dtype=complex)

''' np.zeros((m, *n)) prints the null matrix of specified m and n '''
''' dtype can also be specified here but it's not mandatory '''
print(np.zeros(4))
print(np.zeros(3, dtype=np.int64))
print(np.zeros((4, 6), dtype=np.complex128))

''' np.ones((m, *n)) prints the identity matrix of specified m and n '''
''' dtype can also be specified here but it's not mandatory '''
print(np.ones(4))
print(np.ones(3, dtype=np.int64))
print(np.ones((4, 6), dtype=np.complex128))

''' np.random.random(m ,n) gives random number between 0 and 1 in the
    form of m by n '''
print(np.random.random((2, 3)))
print(np.random.random((3, 2)) * 6)

''' np.sum() prints the sum of elements in an array '''
''' This method is applicable only on numeric arrays '''
print(arr.sum())
print(matrix[0].sum())

''' np.max() prints the maximum number from an array '''
''' This method is applicable only on numeric arrays '''
print(arr.max())
print(matrix[1].max())

''' np.min() prints the minimum number from an array '''
''' This method is applicable only on numeric arrays '''
print(arr.min())
print(matrix[1].min())

''' Use case of np.min(), np.max(), np.max() with axis paramter '''
''' We can pass an optional parameter named 'axis' in these functions '''
print(float_arr.sum(axis=0))
print(float_arr.sum(axis=1))
print(complex_arr.sum(axis=0).sum())
print(complex_arr.max(axis=1))
print(matrix3.min(axis=1))
print(matrix3.min(axis=0))

''' np.sqrt(np.array(...)) prints the sqare root of all the elemen in an array '''
print(np.sqrt(arr))

''' np.std(np.array(...)) finds the standard deviation of an array '''
print(np.std([2, 8, 4, 6]))