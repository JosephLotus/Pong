from turtle import Turtle
FONT = ("Courier", 40, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(0, 230)
        self.write(f"{self.left_score} : {self.right_score}", move=True, align=ALIGNMENT,
                   font=FONT)

    def left_scores(self):
        self.left_score += 1
        self.refresh()

    def right_scores(self):
        self.right_score += 1
        self.refresh()

    def game_over_text(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=True, align=ALIGNMENT,
                   font=FONT)
