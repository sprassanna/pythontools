from tkinter import *

window = Tk()
window.title('GUI ')
window.minsize(width=400, height=100)

label = Label(text='Hello Welcome to Python')
label.pack(side='top')
label.grid(column=0,row=0)

def button_clicked():
    label['text'] = entry.get()
    entry.delete(0,'end')


button = Button(text='Click me ', command=button_clicked)
button.grid(column=1,row=1)

button = Button(text='New button ')
button.grid(column=2,row=0)

entry = Entry(width=15)
entry.grid(column=2,row=2)


window.mainloop()
