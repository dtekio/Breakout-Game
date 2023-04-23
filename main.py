from turtle import Screen
import turtle
from brick import Brick
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

INITIAL_PADDLE_POSITION = (0, -320)
INITIAL_BALL_POSITION = (0, -305)
VERTICAL_LIMIT = 385
HORIZONTAL_LIMIT = 720

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.listen()
screen.tracer(0)

paddle = Paddle((0, -270))
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(key="Left", fun=paddle.left)
screen.onkeypress(key="Right", fun=paddle.right)

brick_x_axis = -HORIZONTAL_LIMIT
brick_y_axis = 330
bricks = []
for i in range(7):
    for j in range(23):
        brick = Brick((brick_x_axis, brick_y_axis))
        bricks.append(brick)
        brick_x_axis += 65
    brick_x_axis = -HORIZONTAL_LIMIT
    brick_y_axis -= 20


def game():
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() < -390:
        ball.bounce('-x')

    if ball.xcor() > 390:
        ball.bounce('x')

    if ball.ycor() > 280:
        ball.bounce('y')

    if ball.ycor() < -280:
        screen.bye()

    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce('x')
            brick.hideturtle()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                ball.bounce('x')
            else:
                # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                ball.bounce('x')
                ball.bounce('y')
            bricks.remove(brick)
            scoreboard.increase_score()
            break

    if 100 >= paddle.xcor() - ball.xcor() >= -100 and ball.ycor() < -270:
        ball.bounce_paddle()

    turtle.ontimer(game, 50)


game()

screen.exitonclick()
