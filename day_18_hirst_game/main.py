from turtle import *
import random

all_colors = [
    (236, 235, 231), (238, 229, 234), (228, 238, 231), (228, 233, 239), (237, 39, 115), (139, 27, 73), (220, 160, 58),
     (240, 71, 36), (15, 142, 89), (180, 166, 43)]

colors_strs  = ['red','blue','green','yellow','brown','orange','cyan','black']

# Recruitment : 10 x 10 matrix  circle radius is 20 and space should be 50

tom = Turtle()
tom.speed('fastest')
my_screen = Screen()
my_screen.colormode(255)
x_pos = 0
y_pos = 0

matrix_size = 10

for y_value in range(matrix_size):

    for _ in range(matrix_size):
        tom.dot(20,random.choice(all_colors))
        tom.penup()
        tom.forward(50)
        tom.pendown()
        tom.dot(20,random.choice(all_colors))

    tom.penup()
    y_pos += 50
    tom.goto(x_pos,y_pos)


my_screen.exitonclick()
