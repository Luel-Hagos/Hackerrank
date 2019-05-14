import numpy as np
A=[]
B=[]
n=int(input())
for i in range(n):
    A.append(list(map(int,input().split())))
for i in range(n):
    B.append(list(map(int,input().split())))
a,b=np.array(A),np.array(B)
print(np.dot(a,b))

