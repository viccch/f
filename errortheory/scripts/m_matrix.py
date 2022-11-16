
from ctypes.wintypes import PINT
import numpy
arr = numpy.matrix([1, 0, -3])
arr2 = numpy.matrix([
    [3, 0, 0],
    [0, 4, 0],
    [0, 0, 2]])
arr3 = numpy.mat([1, 0, -3]).transpose()
#arr3 = numpy.mat([0, 3, 3]).transpose()


print(arr)
print(arr2)
print(arr3)

print(numpy.dot(arr, arr2))

print(numpy.dot(numpy.dot(arr, arr2), arr3))
