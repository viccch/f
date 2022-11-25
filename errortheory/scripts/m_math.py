
import numpy

A = numpy.mat(
    [
        [1],
        [1],
        [-1]
    ])
P = numpy.mat(
    [
        [1, 0, 0],
        [0, 1/6, 0],
        [0, 0, 1/3]
    ])
B = numpy.mat([[10], [11], [-3]])

# print(numpy.linalg.inv(P))

N = (A.transpose())*P*A
W = (A.transpose())*P*B
print(N)
print(W)
# x=numpy.linalg.inv(N)*W
# print(x)
# v=A*x-B
# print(v)
# sigma2=(v.transpose())*P*v/3
# print(sigma2)
# sigma2=2.82666667
# Dxx=sigma2*(numpy.linalg.inv(N))
# print(Dxx)
# D=sigma2*P
# print(D)
print("--------------\n")

v = numpy.mat(
    [
        [-1.444444444],
        [-2.44444444],
        [11.55555555555]
    ])

print(v.transpose()*P*v/2)