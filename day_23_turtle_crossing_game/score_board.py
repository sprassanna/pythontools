from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.score_card = ''

        self.goto(-200,270)
        self.write_score()

    def increment(self):
        self.clear()
        self.score = self.score + 1
        self.write_score()

    def write_score(self):
        self.score_card = 'Level ' + str(self.score)
        self.write(self.score_card, align='center', font=FONT)

    def game_ends(self):
        self.clear()
        self.write('GAME ENDS', align='center', font=FONT)
