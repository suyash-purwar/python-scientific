import numpy as np

a = np.array([(2, 5, 8, 1), (9, 4,6, 3)])
print(a[0, 2])
print(a[0, 1:])
print(a[0:, 1:3])

b = np.linspace(1, 5, 10)
print(b.reshape(2, 5))