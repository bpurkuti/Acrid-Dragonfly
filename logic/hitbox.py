import math
import logic.collision

# type: circle = true, rectangle = false

def hitBoxCheck(obj1, obj2):
    signature = obj1.type + obj2.type
    if(signature == 0):
        return logic.collision.twoRectangle(obj1.position, obj2.position)
    elif(signature == 1):

        if(obj1.type):
            circle = obj1
            rectange = obj2
        else:
            circle = obj2
            rectange = obj1

        return logic.collision.rectangleCircle(circle.position, circle.radius, rectange.position)
    else:
        return logic.collision.twoRectangle(obj1.position, obj2.position)

class RectangleHB(object):
    
    def __init__(self, p1, p2, p3, p4):
        self.position = (p1, p2, p3, p4)
        self.type = False

    def didHit(self, targetHB):
        return hitBoxCheck(self, targetHB)

class CircleHB(object):

    def __init__(self, x, y, radius):
        self.position = (x, y)
        self.radius = radius
        self.type = True
    
    def didHit(self, targetHB):
        return hitBoxCheck(self, targetHB)