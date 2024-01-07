from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()

        self.color('white')
        self.goto(0, 200)
        self.write(f"Score= {0}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))

    def update_score(self,score):
        self.clear()
        self.color('white')
        self.write(f"Score= {score}", align="center", font=("Courier", 24, "normal"))




