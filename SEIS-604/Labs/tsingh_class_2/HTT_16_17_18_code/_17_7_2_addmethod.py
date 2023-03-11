# additional example adding midpoint() method

import math
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    # add new method
    def midpoint(self,p):
        new_point = Point((self.x + p.x) / 2, (self.y + p.y) / 2)
        return new_point


def distance(point1, point2):
    xdiff = point2.getX() - point1.getX()
    ydiff = point2.getY() - point1.getY()

    dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
    return dist


p = Point(4, 3)
q = Point(0, 0)
print(distance(p, q))
point_1 = Point(0.0, 47.0)
point_2 = Point(47.0, 0.0)
mid_point = point_1.midpoint(point_2)