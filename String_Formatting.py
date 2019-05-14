def print_formatted(number):
    w=len(bin(number)[2:])
    for i in range(1,number+1):
        inn=str(i)
        k=oct(i)
        k1=str(k[2:])
        h=hex(i).upper()
        h1=str(h[2:])
        b=bin(i)
        b1=str(b[2:])
        print(inn.rjust(w,' '),k1.rjust(w,' '),h1.rjust(w,' '),b1.rjust(w,' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)