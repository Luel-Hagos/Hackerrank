import numpy as np
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(np.inner(np.array(A),np.array(B)))
print(np.outer(np.array(A),np.array(B)))