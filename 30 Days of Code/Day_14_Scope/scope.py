class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0


    def computeDifference(self):

        max_diff = 0
        for i in range( len(self.__elements)-1 ):

            x = self.__elements[i]

            for j in range(i+1, len(self.__elements) ):

                y = self.__elements[j]
                
                max_diff = max(abs( x - y ), max_diff)

        self.maximumDifference = max_diff
        return max_diff



# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)