import re

result = re.match(r'(?P<user>\w+)@(?P<Website>\w+)\.(?P<extension>\w+)', 'testuser@testweb.com')

# print entire match
# 3
print( result.group(0) )

# print the number of subgroups
# testuser
print( len(result.groups() ))

# print first match subgroup
# testweb
print( result.group(1) )

# print the second match subgroup
# com
print( result.group(2) )

# print the third match subgroup
print( result.group(3) )


# print three groups together in terms of python tuple
# ('testuser', 'testweb', 'com')
print( result.group(1,2,3) )

# print all groups together in temrs of python tuple
# ('testuser', 'testweb', 'com')
print( result.groups() )

# print all groups in temrs of python dictionary
# {'user': 'testuser', 'Website': 'testweb', 'extension': 'com'}
print( result.groupdict() )