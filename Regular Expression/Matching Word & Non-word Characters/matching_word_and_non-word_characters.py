
# Method_#1
#Regex_Pattern = r"\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w"	# Do not delete 'r'.

# Method_#2
Regex_Pattern = r"(\w){3}(\W){1}(\w){10}(\W){1}(\w){3}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())