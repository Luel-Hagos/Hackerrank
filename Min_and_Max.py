import numpy as np
N,M=map(int,input().split())
k=[]
for i in range(N):
    k.append(list(map(int,input().split())))
print(np.max(np.min(np.array(k),axis=1)))

