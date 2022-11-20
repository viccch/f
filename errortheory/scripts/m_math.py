
import numpy

A = numpy.mat(
    [[1,-1,0,1],
     [0,1,1,0]])
P = numpy.mat(
    [[1,0,0,0],
    [0,0.5,0,0],
    [0,0,0.5,0],
    [0,0,0,1]])
B=numpy.mat([[0],[-7],[0],[2]])
#N = A*P*(A.transpose())
#print(P*(A.transpose())*B)
D=A*P*B

C=numpy.mat([[2.5,-0.5],[-0.5,1]])
print(D)
print(C)
print(numpy.linalg.inv(C))
print(numpy.linalg.inv(C)*D)
