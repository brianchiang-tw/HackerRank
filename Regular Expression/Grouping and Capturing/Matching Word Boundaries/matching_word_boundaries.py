Regex_Pattern = r'\b[aioueAEIOU][a-zA-Z]*\b'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())