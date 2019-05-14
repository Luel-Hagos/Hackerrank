a=input()
r1,r2,r3,r4,r5=False,False,False,False,False
for i in range(len(a)):
    if a[i].isalpha():
        r1=True
    if a[i].isdigit():
        r2=True
    if a[i].islower():
        r3=True
    if a[i].isupper():
        r4=True
for i in range(len(a)-1):
    if a[i:i+2].isalnum():
        r5=True
print(r5)
print(r1)
print(r2)
print(r3)
print(r4)
