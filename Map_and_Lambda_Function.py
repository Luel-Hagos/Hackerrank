cube=lambda x: x*x*x
def fibonacci(n):
    f1,f2= 0, 1
    for i in range(n):
        yield f1
        f1,f2= f2,f1+f2

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))