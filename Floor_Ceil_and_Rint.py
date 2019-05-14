import numpy
numpy.set_printoptions(sign=' ')
n=list(map(float,input().split()))
my_array= numpy.array(n)
print (numpy.floor(my_array))
print (numpy.ceil(my_array))
print (numpy.rint(my_array))