import turtle


class Polygon:
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name

    def draw(self):
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(90)
        turtle.done()


square = Polygon(4, "square")
print(square.sides)
print(square.name)
square.draw()

