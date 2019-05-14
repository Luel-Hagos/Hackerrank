import numpy

x,y=input().split()
x,y=int(x),int(y)
numpy.set_printoptions(sign=' ')
print(numpy.eye(x,y))

