import numpy

x=list()
y=int(input())
xx=list()
for i in range(y):
    x1=input().split()
    for j in x1:
        x.append(float(j))
    xx.append(x)
    x=list()
result=numpy.linalg.det(xx)
print(round(result,2))

