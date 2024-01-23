from tkinter import *
from ttkbootstrap import *
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox
import pandas as pd
from urllib.parse import urlparse
from random import choice
from string import ascii_letters, digits, punctuation
import json


def find_pass():
    if l_text.get() != '':
        link = l_text.get().strip()
    try:
        with open('userData.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        Messagebox.show_error(title='Error', message='No saved data found.')
        return

    for entry in data:
        if link in entry:
            em = entry[link]['email']
            ps = entry[link]['password']
                
            Messagebox().show_info(title=f'{link}', message=f'Email: {em}\nPassword: {ps}')
            return

    Messagebox.show_error(title='Error', message='No password found for this link.')
    
    


def save():
    if l_text.get() != '' and e_text.get() != '' and p_text.get() != '':
        l_t = l_text.get()
        e_t = e_text.get()
        p_t = p_text.get()
        
        new_data = {
            l_t:{
                'email': e_t,
                'password': p_t
            }
        }
    
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
        
        Messagebox().show_info(title='Save Details', message=f'Saving\nLink:{l_t}\nEmail:{e_t}\nPassword:{p_t}')
    
    
        try:
           with open("userData.json", "r") as f:
               data = json.load(f)
        except FileNotFoundError:
            data = []
        
        data.append(new_data)
        
        with open('userData.json', 'w') as f:
            json.dump(data, f, indent=4)
            
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
link_text.grid(column=1, row=1, padx=1)
link_text.focus()
search_btn = Button(text='Search', bootstyle='warning-outline', width=15,command=find_pass)
search_btn.grid(column=2, row=1)

email_label = Label(text='Username or Email', bootstyle='inverse-success')
email_label.grid(column=0, row=2)
email_text = Entry(textvariable=e_text,bootstyle='warning', width=35)
email_text.grid(column=1, row=2, columnspan=2, pady=10)

pass_label = Label(text='Password', bootstyle='inverse-danger')
pass_label.grid(column=0, row=3)
pass_text = Entry(textvariable=p_text,bootstyle='info', width=35)
pass_text.grid(column=1, row=3)

generate_btn = Button(text='Generate Password', bootstyle='danger-outline', command=generate_password, width=15)
generate_btn.grid(column=2, row=3)

save_btn = Button(text='Save', bootstyle='success', width=36, command=save)
save_btn.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
