class Apple:
    def __init__(self, color, height, width, rot):
        self.color = color
        self.height = height
        self.width = width
        self.rot = rot

    def show_values(self):
        print("Color: {}".format(self.color))
        print("Height: {}".format(self.height))
        print("Width: {}".format(self.width))
        print("Rot: {}".format(self.rot))

apple = Apple("#FF0000", 5, 5.5, 10)
apple.show_values()
