from  string import ascii_lowercase as prince
def print_rangoli(size):
    # your code goes here
    luel=[]
    for i in range(size):
        rangoli= "-".join(prince[i:size])
        luel.append((rangoli[::-1]+rangoli[1:]).center(4*size-3, "-"))
    print('\n'.join(luel[:0:-1]+luel))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)