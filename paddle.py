from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, start_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(start_pos)

    def move_up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)
