class Square():
    squares = []

    def __init__(self, side):
        self.side = side
        self.squares.append(side)

sq = Square(5)
sqr = Square(7)

print(Square.squares)
