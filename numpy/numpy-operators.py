''' Arithmetic operators on arrays apply elementwise.
    A new array is created and filled with the result. '''
    
import numpy as np

matrix1 = np.array([(10, 20), (30, 40), (50, 60)])
matrix2 = np.array([(4, 2), (2, -9), (6, 2)])
array1 = np.array([1, 5, 3, 9])
array2 = np.array([2, 4, 2, 5])
matrix3 = np.array([[10, 2], [12, 7]])
matrix4 = np.array([[4, 17], [-4, 5]])

''' 
    Operations like +, -, *, <, +=, -=, *=, @, ** are available
    with numpy arrays.
    This is the big reason why numpy arrays are more convenient
    
    WARNING: Some of these operators works on multi-dimensional arrays only
'''

print(matrix1 + matrix2)
print(matrix1 - matrix2)
print(matrix1 / matrix2)
print(matrix1 // matrix2)
print(matrix1 < matrix2)
print(matrix2 ** 2)
print(array1 * array2)
print(matrix3 * matrix4)
print(array1 @ array2)
print(matrix3 @ matrix4)
print(matrix3.dot(matrix4))

print(np.vstack((matrix1, matrix2)))
print(np.hstack((matrix1, matrix2)))
print(np.ravel(matrix4))