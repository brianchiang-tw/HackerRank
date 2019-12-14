class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, score):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.score_list = score

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        
        avg = sum( self.score_list )/len(self.score_list)

        if 90 <= avg <= 100:
            #print("O")
            level = "O"

        elif 80 <= avg:
            #print("E")
            level = "E"

        elif 70 <= avg:
            #print("A")
            level = "A"

        elif 55 <= avg:
            #print("P")
            level = "P"

        elif 40 <= avg:
            #print("D")
            level = "D"
        
        else:
            #print("T")
            level = "T"
        '''
        O     90, 100
        E    80, 90
        A    70, 80
        P    55, 70
        D    40, 55
        T    <40
        '''


        return level



line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())