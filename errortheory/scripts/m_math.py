
import numpy

A = numpy.mat(
    [[0,0,1,0,-1,-1],
     [1,1,1,0,0,0],
     [0,-1,0,1,0,-1]])
P = numpy.eye(6)
B=numpy.mat([[5.25],[0],[-3.75]])
#N = A*P*(A.transpose())
print(P*(A.transpose())*B)
