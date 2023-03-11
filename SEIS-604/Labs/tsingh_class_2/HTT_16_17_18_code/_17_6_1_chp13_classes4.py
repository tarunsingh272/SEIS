#
# HTT Ch 17 code example:
#
# Section 17.6, example 1: chp13_classes4
#

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

p = Point(7, 47)

print(p.getX())
print(p.getY())
print(p.y)
