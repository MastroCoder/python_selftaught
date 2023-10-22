import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)

circle = Circle(5)
print("Area: %.2f" % circle.area())
