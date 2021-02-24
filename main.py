from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_over = False

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()

    # Detect collision with top/bot wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vert_bounce()

    # Detect collision with paddle
    if (ball.xcor() == 330 and ball.distance(r_paddle) < 60) or (ball.xcor() == -330 and ball.distance(l_paddle) < 60):
        ball.horiz_bounce()

    # Detect if left scores
    if ball.xcor() > 400:
        scoreboard.left_scores()
        if scoreboard.left_score == 7:
            scoreboard.game_over_text()
            game_over = True
        ball.ball_reset()

    # Detect if right scores
    elif ball.xcor() < -400:
        scoreboard.right_scores()
        if scoreboard.right_score == 7:
            scoreboard.game_over_text()
            game_over = True
        ball.ball_reset()

screen.exitonclick()
