# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---- Generate password and store it in text file for each site --- #
from tkinter import *
from tkinter import messagebox
from password_generator import  PasswordGenerator
import pyperclip
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # add to a file

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) > 0  and len(email) >0 and len(password) >0 :
        is_all_ok = messagebox.askokcancel(title='Confirm',message=f' Url: {website} \n Email: {email} \n Password: {password} \n  is it ok?')

        if is_all_ok:
            f = open("data.txt", "a")
            f.write(f'{website} | {email} | {password} \n')
            f.close()

            #clean up entries
            website_entry.delete(0,END)
            password_entry.delete(0,END)

    else:
        messagebox.showerror('Error',message='Enter required fields')
# ---------------------------- UI SETUP ------------------------------- #

def generate_password():
    password_entry.delete(0,END)
    password_gen = PasswordGenerator()
    pwd = password_gen.generate_password()
    pyperclip.copy(pwd)
    password_entry.insert(0,pwd)


window = Tk()
window.title('Password manager')
window.minsize(200, 200)
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text='Email/UserName:')
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'iamprassanna@gmail.com')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text='Generate Password',command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
