import numpy 
N,k=map(int,input().split())

a= numpy.array([input().split() for i in range(N)], int)
b= numpy.array([input().split() for i in range(N)], int)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

