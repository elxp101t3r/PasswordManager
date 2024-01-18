from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox
import pandas as pd
from urllib.parse import urlparse
from random import choice
from string import ascii_letters, digits, punctuation


def save():
    if l_text.get() != '' and e_text.get() != '' and p_text.get() != '':
        l_t = l_text.get()
        e_t = e_text.get()
        p_t = p_text.get()
    
        if not l_t.startswith('https'):
            l_t = 'https://' + l_t
        try:
            result = urlparse(l_t)
            if not all([result.scheme, result.netloc]):
                Messagebox.show_error(title='Enter Valid Link', message='Please enter valid link.')
                l_text.set('')
                return
        except ValueError:
            Messagebox.show_error(title="Link", message='Please enter a valid link.')
            return
            
            
        user_data = {
            'Link': l_t,
            'Email/Uname': e_t,
            'Password': p_t 
        }
        
        
        Messagebox().show_info(title='Save Details', message=f'Saving\nLink:{l_t}\nEmail:{e_t}\nPassword:{p_t}')
    
    
        try:
            df = pd.read_excel('password_manager.xlsx', engine='openpyxl')
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Link', 'Email/Uname', 'Password'])
        
        new_row = pd.DataFrame(user_data, index=[len(df)+1])
        df = pd.concat([df, new_row], ignore_index=True)
            
        with pd.ExcelWriter('password_manager.xlsx', engine='openpyxl', mode='w') as writer:
            df.to_excel(writer, index=False)
            
        l_text.set('')
        p_text.set('')
    elif l_text.get() == '' or e_text.get() == '' or p_text.get() == '':
        Messagebox.show_error(title='Fill Fields', message="Please fill out all fields.")
          
    l_text.set('')
    p_text.set('')

    
def generate_password(): 
    alphabet = ascii_letters + digits + punctuation
    p_text.set(''.join(choice(alphabet) for _ in range(12)))
   
      
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

generate_btn = Button(text='Generate Password', bootstyle='danger-outline', command=generate_password)
generate_btn.grid(column=2, row=3)

save_btn = Button(text='Save', bootstyle='success', width=36, command=save)
save_btn.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
