from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()

        self.color('white')
        self.goto(0, 200)
        self.write(f"Score= {0} high score = {self.read_highscore()}", align="center", font=("Courier", 24, "normal"))

    def update_highscore(self):
        print(f'{self.high_score}')
        with open('data.txt', mode='w') as data:
            data.write(str(self.high_score))

    def read_highscore(self):
        with open('data.txt', mode='r') as data:
            return int(data.read())

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        print(f'Updating score {self.high_score}')
        self.update_highscore()

        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.color('white')
        self.write(f"Score= {self.score} high score = {self.read_highscore()}", align="center",
                   font=("Courier", 24, "normal"))
