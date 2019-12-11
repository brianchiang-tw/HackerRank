# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':

    # n: number of students
    # x: number of subjects
    n, x = map(int, input().split() )

    subject_score = [ []*n ] * x

    for i in range(x):

        subject_score[i] = list(map(float, input().split() ) )


    # get the list of student score
    student_score = zip( *subject_score )

    # output the average score for each student
    for s in student_score:

        print( sum(s) / x)
