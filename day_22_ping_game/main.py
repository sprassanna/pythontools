from turtle import Screen,Turtle
import time

from paddle import Paddle
from ball import Ball

from scoreboard import  ScoreBoard
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.tracer(0)

scoreboard = ScoreBoard()


r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()


screen.listen()

screen.onkeypress(r_paddle.up,'Up')
screen.onkeypress(r_paddle.down,'Down')


screen.onkeypress(l_paddle.up,'w')
screen.onkeypress(l_paddle.down,'s')

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    if ball.xcor() > 350:
        ball.move_to_centre()
        scoreboard.l_point()
        ball.bounce_x()
        ball.move()

    if ball.xcor() < -350:
        ball.move_to_centre()

        scoreboard.r_point()
        ball.bounce_x()
        ball.move()




screen.exitonclick()
