import pandas as pd

 user_data = {
        'Link': l_text.get(),
        'Email/Uname': e_text.get(),
        'Password': p_text.get()
    }
    df = pd.DataFrame(user_data, index=[x for x in range(1, len(user_data)+1)])

with pd.ExcelWriter('password_manager.xlsx', engine='openpyxl', mode='a') as writer:
    df.to_excel(writer)