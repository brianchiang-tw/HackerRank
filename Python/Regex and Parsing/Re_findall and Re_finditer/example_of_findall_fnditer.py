import re

result = re.findall(r'\w',"http://www.google.com")

print( result )

result = re.finditer(r'\w', "http://www.google.com" )


# result is a callable iterator object
print( result )

# convert result to a list of matches
all_matches = list( map( lambda x:x.group(), result ) )
print( all_matches )

