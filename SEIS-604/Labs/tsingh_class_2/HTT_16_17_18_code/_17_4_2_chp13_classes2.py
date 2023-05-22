#
# HTT Ch 17 code example:
#
# Section 17.4, example 1: chp13_classes2 + mods
#

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)

# we need to teach Point how to return its str image, instead of this default one
#  we also show the id (address) of each object:

# => we have two Point objects, each occupying a different place in memory

print(q, id(q))
print(p, id(p))

# p is NOT the same object as q:

print(p is q)
