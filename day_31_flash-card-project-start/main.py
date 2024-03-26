BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

ORIGINAL = './data/french_words.csv'
NEW_FILE = './data/words_to_learn.csv'

data_frame = None
try:
    data_frame = pd.read_csv(NEW_FILE)
except FileNotFoundError:
    data_frame = pd.read_csv(ORIGINAL)

data_dict = data_frame.to_dict(orient='records')

new_card = {}


def pick_new_word():
    global new_card, flip_timer

    window.after_cancel(flip_timer)

    new_card = random.choice(data_dict)
    canvas.itemconfig(french_word, text='French', fill='black')
    canvas.itemconfig(english_word, text=f'{new_card['French']}', fill='black')
    canvas.itemconfig(card_background, image=front_photo)
    flip_timer = window.after(3000, flip_card)


def move_on():
    data_dict.remove(new_card)
    new_df = pd.DataFrame(data_dict)
    new_df.to_csv(NEW_FILE, index=False)
    pick_new_word()


def flip_card():
    canvas.itemconfig(french_word, text='English', fill='yellow')
    canvas.itemconfig(english_word, text=f'{new_card['English']}', fill='yellow')
    canvas.itemconfig(card_background, image=back_photo)


window = Tk()
window.title('Flash Game')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

front_photo = PhotoImage(file='./images/card_front.png')
back_photo = PhotoImage(file='./images/card_back.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 283, image=front_photo)

french_word = canvas.create_text(400, 150, text='Title', font=('Arial', 25, 'italic'))
english_word = canvas.create_text(400, 283, text='word', font=('Arial', 40, 'bold'))

canvas.grid(row=0, column=0, columnspan=2)

cancel_image = PhotoImage(file='./images/wrong.png')
cancel_button = Button(image=cancel_image, command=pick_new_word)
cancel_button.grid(row=1, column=0)

correct_image = PhotoImage(file='./images/right.png')
right_button = Button(image=correct_image, command=move_on)
right_button.grid(row=1, column=1)

pick_new_word()

window.mainloop()
