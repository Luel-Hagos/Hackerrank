# Enter your code here. Read input from STDIN. Print output to S
import re
prince=re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
for i in range(int(input())):
    print(bool(prince.match(input())))
