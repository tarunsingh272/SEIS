#
# HTT Ch 17 code example:
#
# Section 17.5, example 1: chp13_improveconstructor (CodeLens)
#

class Point:
	""" Point class for representing and manipulating x,y coordinates. """

	def __init__(self, initX, initY):
		""" Create a new point at the given coordinates. """
		self.x = initX
		self.y = initY

p = Point(7, 6)

input("pause within Python Tutor to examine p...")