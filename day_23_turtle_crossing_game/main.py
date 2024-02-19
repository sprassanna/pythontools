import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carManager = CarManager()

screen.listen()
screen.onkeypress(player.move_fwd, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    carManager.create_car()
    carManager.move_left()

    for car in carManager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_ends()

    if player.ycor() >= 280:
        player.reset_player()
        scoreboard.increment()
        carManager.move_fast()

    screen.update()


screen.exitonclick()
