class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

class Square():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

sq = Square(5)
rect = Rectangle(6, 3)

print("Perímetro retângulo: {}\n Perímetro quadrado: {}".format(sq.calculate_perimeter(),
                                                                rect.calculate_perimeter()))
