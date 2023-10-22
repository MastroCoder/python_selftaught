class Hexagon:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side * 6

hexagon = Hexagon(8)

print("Perímetro = {}".format(hexagon.perimeter()))
