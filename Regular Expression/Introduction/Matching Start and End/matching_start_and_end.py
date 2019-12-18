
# Method_#1
#Regex_Pattern = r"^\d\w\w\w\w\.$"	# Do not delete 'r'.

# Method_#2
Regex_Pattern = r"^(\d)(\w){4}(\.)$"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())