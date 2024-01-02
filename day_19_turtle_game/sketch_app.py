from turtle import *

jerry = Turtle()
screen = Screen()
jerry.speed('fastest')


def move_forward():
    jerry.forward(200)


def clear_screen():
    screen.clear()


def move_backward():
    jerry.backward(200)


def rotate_clockwise():
    jerry.right(45)
    jerry.circle(100)


def rotate_counter_clockwise():
    jerry.left(45)
    jerry.circle(100)


def draw_sketches():
    screen.listen()
    screen.onkey(move_forward, 'f')
    screen.onkey(move_backward, 'b')
    screen.onkey(rotate_clockwise,'d')
    screen.onkey(rotate_counter_clockwise,'a')
    screen.onkey(clear_screen,'c')
    screen.exitonclick()
