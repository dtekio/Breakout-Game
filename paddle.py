from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.create_paddle(pos)

    def create_paddle(self, pos):
        self.goto(pos)

    def left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def right(self):
        self.goto(self.xcor() + 20, self.ycor())
