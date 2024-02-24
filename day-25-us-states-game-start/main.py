from turtle import Turtle, Screen
import pandas as pd

timmy = Turtle()
screen = Screen()
screen.setup(width=1000, height=600)
image = "blank_states_img.gif"
screen.addshape(image)
timmy.shape(image)

states_data = pd.read_csv('50_states.csv')
correct_guesses = []
states_list = states_data.state.tolist()
filtered_data_row = []

while len(correct_guesses) <= 50:
    answer_check = screen.textinput(title=f"{len(correct_guesses)}/states Correct", prompt="Guess the state").title()

    print(answer_check)
    if answer_check == 'Exit':
        break
    correct_guesses.append(answer_check)

    name_card = Turtle()
    name_card.penup()
    name_card.hideturtle()
    highlighted_row = states_data[states_data.state == answer_check]
    name_card.goto(int(highlighted_row.x), int(highlighted_row.y))
    name_card.write(answer_check, align="center", font=("Arial", 16, "normal"))

for index,row in states_data.iterrows() :
    if row.state in correct_guesses:
        pass
    else:
        filtered_data_row.append(row)
pd.DataFrame(filtered_data_row).to_csv('new_filtered_data.csv')
