from collections import namedtuple

n, name_tuple_stu = int(input()), namedtuple('Student', input().split() )
student_list = [ name_tuple_stu( *input().split() ) for _ in range(n) ]
print('{:.2f}'.format(  sum( [int(stu.MARKS) for stu in student_list] ) / n )  )