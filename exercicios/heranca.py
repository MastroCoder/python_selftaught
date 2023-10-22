class Shape():
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return (self.width + self.length) * 2

    def what_am_i(self):
        print("I am a shape!")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

sq = Square(5, 5)
rect = Rectangle(6, 3)

print("Perímetro retângulo: {}\nPerímetro quadrado: {}".format(sq.calculate_perimeter(),
                                                                rect.calculate_perimeter()))

sq.what_am_i()
rect.what_am_i()
