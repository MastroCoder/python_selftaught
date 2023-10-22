class Square():
    squares = []

    def __init__(self, side):
        self.side = side
        self.squares.append(side)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)

sq = Square(79)
print(sq)
