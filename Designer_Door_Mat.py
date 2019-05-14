N,M= map(int,input().split())
for i in range(int(N/2)):
    print(('.|.'*(2*i + 1)).center(M, '-'))
print('WELCOME'.center(M,'-'))
for i in range(int(N/2),-1,-1):
    if i==int(N/2):
        continue
    print(('.|.'*(2*i + 1)).center(M, '-')