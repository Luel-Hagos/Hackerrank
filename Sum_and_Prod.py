import numpy as np
k=[]
N,M=map(int,input().split())
for i in range(N):
    k.append(list(map(int,input().split())))
    
l=np.array(k)
h=np.sum(l,axis=0)
print(np.product(h))