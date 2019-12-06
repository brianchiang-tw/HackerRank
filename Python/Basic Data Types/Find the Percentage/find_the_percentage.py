
from typing import Dict

def get_average_of_student( stu_dict:Dict, name:str)->float:

    # get the grade list of student
    grade_of_student = stu_dict[name]

    # compute the average grade
    average_grade = sum(grade_of_student)/len(grade_of_student)

    return average_grade




if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    avg = get_average_of_student( student_marks, query_name)
    print( "%.2f" % avg )
