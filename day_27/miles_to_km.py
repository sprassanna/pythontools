from tkinter import *

window = Tk()
window.title('Miles to Kilometre')
window.minsize(width=300,height=200)


def convert_to_km():
    miles_value = text_input.get()
    kms_value = (int(miles_value) * 1.609)
    km_value.config(text=kms_value)

text_input = Entry()
text_input.grid(row=0,column=1)

miles_label = Label(text='miles')
miles_label.grid(row=0,column=2)

equal_to_label = Label(text='is equal to')
equal_to_label.grid(row=1,column=0)

km_value = Label(text='0')
km_value.grid(row=1,column=1)

km_label = Label(text='Km')
km_label.grid(row=1,column=2)

calculate = Button(text='Calculate',command=convert_to_km)
calculate.grid(row=2,column=1)






window.mainloop()
