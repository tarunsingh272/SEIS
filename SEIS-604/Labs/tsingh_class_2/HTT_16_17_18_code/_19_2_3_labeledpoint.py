# _19_2_3_labeledpoint_2.py

import _19_2_1_pointclass_1 as p # not needed in notebook

class LabeledPoint(p.Point):

    def __init__(self, initX, initY, label):
        self.x = initX
        self.y = initY
        self.label = label

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y) + " (" + self.label + ")"

labeledPt = LabeledPoint(7,6,"Here")
print(labeledPt)
