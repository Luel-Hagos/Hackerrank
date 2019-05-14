import numpy as np
np.set_printoptions(legacy='1.13')
N,M=map(int,input().split())
k=[]
for i in range(N):
    k.append(list(map(int,input().split())))
print(np.mean(np.array(k),axis=1))
print(np.var(np.array(k),axis=0))
print(np.std(np.array(k)))