
# Method_#1
#Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

# Method_#2
Regex_Pattern = r"(\S\S\s){2}(\S\S){1}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())