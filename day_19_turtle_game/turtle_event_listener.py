from turtle import *

tim = Turtle()
tim.speed('slowest')
screen = Screen()



def move_forward():
    tim.forward(10)


def show_and_move_tutle():

    screen.listen()
    screen.onkey(move_forward,'space')
    screen.exitonclick()


