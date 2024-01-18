from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100,image=logo)
canvas.grid(column=1, row=0)

link_label = Label(text='Link', bootstyle='inverse-default')
link_label.grid(column=0, row=1)
link_text = Entry(bootstyle='success', width=35)
link_text.grid(column=1, row=1, columnspan=2, padx=10)

email_label = Label(text='Username or Email', bootstyle='inverse-success')
email_label.grid(column=0, row=2)
email_text = Entry(bootstyle='warning', width=35)
email_text.grid(column=1, row=2, columnspan=2, pady=10)





window.mainloop()
