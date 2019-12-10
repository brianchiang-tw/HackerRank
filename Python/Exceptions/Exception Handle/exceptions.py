# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int( input() )

for _ in range(n):

    buf = input().split()

    try:
        a, b = int( buf[0] ), int( buf[1] )
        quotient = a / b 
        print( int(quotient) )

    except ZeroDivisionError as e:
        print("Error Code: " + "integer division or modulo by zero" )

    except ValueError as e:
        print("Error Code: " + str(e) )