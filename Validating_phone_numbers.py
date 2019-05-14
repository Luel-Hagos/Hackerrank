import re
n=int(input())
for i in range(n):
    try:
        k=input()
        match=re.match(r'[789]\d{9}$',k)
        if match:
            print('YES')
        else:
            print('NO')
    except:
        print('NO')