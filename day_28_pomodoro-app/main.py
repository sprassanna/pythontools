from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.25
LONG_BREAK_MIN = 1

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="TIMER",fg=GREEN)
    tick_label.config(text='')
    canvas.itemconfig(timer_text, text=f'00:00')
    global reps
    reps =0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps


    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    reps += 1

    print(f'reps : {reps}')
    if reps % 8 == 0 :
        count_down(long_break_sec)
        timer_label.config(text='Long Break',fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Short Break', fg=GREEN)
    else:
        count_down(work_sec)
        timer_label.config(text='WORK', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec <10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count >0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ''
        for index in range(math.floor(reps/2)):
            marks += "✅"
        tick_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomorodo App')
window.config(padx=50,pady=5,bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW,)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100,90,image=tomato_image)
timer_text = canvas.create_text(104,112,text='00:00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(row = 1 , column =1)


timer_label = Label(text='TIMER',fg=GREEN, bg=YELLOW ,font=(FONT_NAME,70,'bold'))
timer_label.grid(row=0,columns =2)



start_button = Button(text ='Start',command=start_timer)
start_button.grid(row=2,column=0)


tick_label = Label()
tick_label.grid(row=2,columns =2)

reset_button = Button(text ='Reset',command=reset_timer)
reset_button.grid(row=2,column=2)

window.mainloop()
