i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
int_val = None
float_val = None
str_val = None
# Read and save an integer, double, and String to your variables.
int_val = int( input() )
float_val = float( input() )
str_val = input()


# Print the sum of both integer variables on a new line.
print( i + int_val )
# Print the sum of the double variables on a new line.
print( "%1.1f" % ( i + float_val ) )
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print( "HackerRank " + str_val )
