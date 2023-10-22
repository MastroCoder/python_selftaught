class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return (self.base * self.height) / 2

triangle = Triangle(3, 4)

print("Área: {}".format(triangle.area()))
