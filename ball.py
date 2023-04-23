from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.025
        self.setheading(45)
        self.goto(-120, -280)

    def move(self):
        self.forward(10)

    def bounce(self, pos):
        if pos=="x":
            self.setheading(180 - self.heading())
        elif pos=='-x':
            self.setheading(180 - self.heading())
        elif pos=='y':
            self.setheading(360 - self.heading())

    def bounce_paddle(self):
        self.setheading(360 - self.heading())
        self.move_speed *= 0.9
