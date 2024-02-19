from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.move = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.create_car()

    def create_car(self):
        random_choice = random.randint(1,10)
        if random_choice == 1 :
            new_car = Turtle()
            new_car.penup()
            new_car_y_pos = random.randint(-280, 280)
            new_car.shape('square')
            new_car.shapesize(stretch_len=3, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(280, new_car_y_pos)

            self.all_cars.append(new_car)

    def move_left(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.move
            car.goto(new_x,car.ycor())

    def move_fast(self):
        self.move = self.move + MOVE_INCREMENT
        self.move_left()
