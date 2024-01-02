from turtle import *
import random

screen = Screen()
turtle_colors = ['red','yellow','purple','orange','cyan','green']
y_position = [-100,-70,-40,-10,30,60,90]
all_turtles = []


def start_the_game():
    global new_turtle
    screen.setup(width=500, height=400)
    user_choice = screen.textinput(title='Chose a color?',prompt='Color')
    print(f'user choice is {user_choice}')
    is_game_on = True

    for index in range(0,len(turtle_colors)):
        new_turtle = Turtle(shape='turtle')
        new_turtle.speed('slowest')
        new_turtle.penup()
        new_turtle.color(turtle_colors[index])
        new_turtle.goto(x=-230, y=y_position[index])
        new_turtle.xcor()
        all_turtles.append(new_turtle)

    while is_game_on:
        for turtle in all_turtles:
            if turtle.xcor() > 250:
                is_game_on = False
                winning_color = turtle.pencolor()
                if user_choice ==  winning_color:
                    print(f'You have won {winning_color} is the winning_color')
                else:
                    print(f'You have lost {winning_color} is the winning_color')
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)



    screen.exitonclick()






