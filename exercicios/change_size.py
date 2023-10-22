class Square():
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4

    def change_size(self, added_side):
        self.side += added_side

    def get_side(self):
        return self.side


sq = Square(7)
print("Lado atual: {}".format(sq.get_side()))
sq.change_size(7)
print("Lado pós mudança: {}".format(sq.get_side()))
