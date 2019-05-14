import numpy
n=list(map(int,input().split()))
k=int(n[0])+int(n[1])
m=[]
array_2=[]
for i in range(k):
    l=list(map(int,input().split()))
    m.append(l)
m=numpy.array(m)
array_2=numpy.concatenate((m))
print(m)
