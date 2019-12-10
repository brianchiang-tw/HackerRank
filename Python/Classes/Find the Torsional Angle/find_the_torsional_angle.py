import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def __sub__(self, no):

        result_x, result_y, result_z = self.x - no.x, self.y - no.y, self.z - no.z
        return Points( result_x, result_y, result_z )


    def dot(self, no):

        return ( self.x * no. x + self.y * no.y + self.z * no.z )

    def cross(self, no):

        result_x = self.y * no.z - no.y * self.z
        result_y = -( self.x * no.z - no.x * self.z )
        result_z = self.x * no.y - no.x * self.y

        return Points( result_x, result_y, result_z )

        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':