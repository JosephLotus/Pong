from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.08

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def vert_bounce(self):
        self.y_move *= -1

    def horiz_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.horiz_bounce()
        self.move_speed = 0.08
        time.sleep(0.5)
