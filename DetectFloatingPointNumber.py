import re
prince=re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
 print(bool(prince.match(input())))
for i in range(int(input())):