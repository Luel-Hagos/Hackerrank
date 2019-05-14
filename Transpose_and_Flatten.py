import numpy
n=list(map(int,input().split()))
n1=int(n[0])
k=[]
for i in range(n1):
    m=list(map(int,input().split()))
    k.append(m)

my_array = numpy.array(k)
print (numpy.transpose(my_array))
print(my_array.flatten())
