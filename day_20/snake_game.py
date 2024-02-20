from turtle import Turtle, Screen
import time
from food import Food
from scoreboard import ScoreBoard

from snake import Snake

turtle = Turtle()
screen = Screen()

screen.title('My Snake Game')
screen.setup(width=500, height=500)
screen.bgcolor('black')


def start_game():
    is_game_on = True
    screen.tracer(0)
    food = Food()
    score = ScoreBoard()
    snake = Snake()
    screen.listen()
    score_count = 0
    screen.onkeypress(snake.up, 'Up')
    screen.onkeypress(snake.down, 'Down')
    screen.onkeypress(snake.left, 'Left')
    screen.onkeypress(snake.right, 'Right')

    while is_game_on:
        screen.update()
        time.sleep(0.2)
        snake.move()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.append_a_segment()

            score.update_score()

        if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
            score.reset_score()
            snake.reset_snake()

        for segment in snake.segments[1:]:
            if segment.distance(snake.head) <= 10:
                score.reset_score()
                snake.reset_snake()

    screen.exitonclick()
