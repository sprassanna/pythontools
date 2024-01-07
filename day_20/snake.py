from turtle import *

INTIAL_RANGE = [(0, 0), (-20, 0), (-40, 0)]

UP = 90

DOWN = 270

LEFT = 180

RIGHT =0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for index in range(3):
            new_segment = self.create_new_segment()
            new_segment.setposition(INTIAL_RANGE[index])

            self.segments.append(new_segment)

    def create_new_segment(self):

        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.speed('fast')

        new_segment.color('white')
        return new_segment

    def append_a_segment(self):
        new_segment = self.create_new_segment()
        self.segments.append(new_segment)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)
            self.move()

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)
            self.move()

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(0)
            self.move()
