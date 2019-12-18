# Method_#1
#Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	

# Method_#2
Regex_Pattern = r'(\d\d\D){2}(\d\d\d\d)'


import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())