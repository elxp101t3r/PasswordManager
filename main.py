from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
import pandas as pd


def save():
    user_data = {
        'Link': l_text.get(),
        'Email/Uname': e_text.get(),
        'Password': p_text.get()
    }
    
    try:
        df = pd.read_excel('password_manager.xlsx', engine='openpyxl')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Link', 'Email/Uname', 'Password'])
    
    new_row = pd.DataFrame(user_data, index=[len(df)+1])
    df = pd.concat([df, new_row], ignore_index=True)
    
    with pd.ExcelWriter('password_manager.xlsx', engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, index=False)
    
    l_text.set('')
    e_text.set('')
    p_text.set('')
    

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100,image=logo)
canvas.grid(column=1, row=0)

l_text = StringVar()
e_text = StringVar()
p_text = StringVar()

link_label = Label(text='Link', bootstyle='inverse-default')
link_label.grid(column=0, row=1)
link_text = Entry(textvariable=l_text,bootstyle='success', width=35)
link_text.grid(column=1, row=1, columnspan=2, padx=10)
link_text.focus()

email_label = Label(text='Username or Email', bootstyle='inverse-success')
email_label.grid(column=0, row=2)
email_text = Entry(textvariable=e_text,bootstyle='warning', width=35)
email_text.grid(column=1, row=2, columnspan=2, pady=10)

pass_label = Label(text='Password', bootstyle='inverse-danger')
pass_label.grid(column=0, row=3)
pass_text = Entry(textvariable=p_text,bootstyle='info', width=21)
pass_text.grid(column=1, row=3)

generate_btn = Button(text='Generate Password', bootstyle='danger-outline')
generate_btn.grid(column=2, row=3)

save_btn = Button(text='Save', bootstyle='success', width=36, command=save)
save_btn.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
