def get_the_2nd_lower( stu_list ):

    min_grade = min( stu_list, key = lambda x: x[1])[1]
    #print( min_grade )

    stu_list_without_lowest = [ s for s in stu_list if s[1] != min_grade]


    # sort with student's name of ascending order
    stu_list_without_lowest.sort( key = lambda x:x[0])

    # get second lower grade
    second_lower = min( stu_list_without_lowest, key = lambda x: x[1])[1]

    for s in stu_list_without_lowest:
        #print( s[0] )
        #print( s[1] )
        if s[1] == second_lower:
            print(s[0])

    return




if __name__ == '__main__':

    student_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        student_list.append( list([name, score]) )

    get_the_2nd_lower( student_list )
