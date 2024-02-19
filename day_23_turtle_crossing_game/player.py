from turtle import  Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.shape('turtle')
        self.left(90)
        self.reset_player()

    def reset_player(self):
        self.setposition(STARTING_POSITION)

    def move_fwd(self):
        new_y_cord = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y_cord)


