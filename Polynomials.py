import numpy

x=list()
x1=input().split()
y=int(input())
for i in x1:
    x.append(float(i))
print (numpy.polyval(x, y))
