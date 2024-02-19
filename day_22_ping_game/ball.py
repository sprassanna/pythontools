from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_to_centre()
        self.move_speed = 0.1

        self.x_mov = 10
        self.y_mov = 10

    def move_to_centre(self):
        self.setposition(0, 0)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov

        if new_x >= 290:
            new_y = self.ycor() - 10

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_mov *= -1

    def bounce_x(self):
        self.move_speed *= 0.5
        self.x_mov *= -1
