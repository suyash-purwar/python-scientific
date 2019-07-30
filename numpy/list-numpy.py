import numpy as np
import sys
import time

array = np.array([3, 4, 1, 4, 9])
matrix = np.array([
            (1, 2, 3), 
            (4, 5, 6),
            (7, 8, 9)
        ])

pylist = range(0, 500)
nplist = np.arange(0, 500)

size_of_pylist = sys.getsizeof(pylist) * len(pylist)
size_of_nplist = nplist.size * nplist.itemsize

SIZE = 100000

list1 = list2 = range(SIZE)
start = time.time()
result = [(x + y) for x, y in zip(list1, list2)]

print((time.time() - start) * 1000)

numpy1 = numpy2 = np.arange(SIZE)
start = time.time()
result = numpy1 + numpy2
print((time.time() - start) * 1000)