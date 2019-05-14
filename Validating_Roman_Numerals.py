regex_pattern = r"^M{,3}(D?C{,3}|C?D|CM)?(L?X{,3}|X?L|XC)?(V?I{,3}|I?V|IX)?$"	
# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))