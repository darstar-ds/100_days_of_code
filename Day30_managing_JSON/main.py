import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

WHITE="#FFFFFF"
LABEL_FONT=("Arial", 12, "bold")
BUTTON_FONT=("Arial", 10, "bold")
# ---------------------------- SEARCH PASSWORD ---------------------------------- #

def search_password():
    try:
        with open("./Day30_managing_JSON/my_pass.json", "r") as passfile:
            
            data = json.load(passfile)
            website=entry_website.get()
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
    except FileNotFoundError:
        messagebox.showwarning(title="No data file", message="No password file found!")        
    except KeyError:
        messagebox.showwarning("keyerror", f"No such website ({website}) in the password file.")
    
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_list_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_list_letters + password_list_symbols + password_list_numbers

    print(password_list)
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_pass.delete(0, "end")
    entry_pass.insert(0, password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website=entry_website.get()
    email=entry_email.get()
    password=entry_pass.get()
    new_data = {
        website:
            {"email": email,
             "password": password} 
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showwarning(title="Ooops", message="Don't leave any fields empty!")
        pass
    else:
        is_OK = messagebox.askokcancel(title=website, 
                                        message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\nIs it OK to save?")
        
        if is_OK:
            try:
                with open("./Day30_managing_JSON/my_pass.json", "r") as passfile:
                    # Reading old data
                    data = json.load(passfile)
                    #Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open("./Day30_managing_JSON/my_pass.json", "w") as passfile:
                    #Saving updated data
                    json.dump(new_data, passfile, indent=4)
            else:
                with open("./Day30_managing_JSON/my_pass.json", "w") as passfile:
                    #Saving updated data
                    json.dump(data, passfile, indent=4)
            finally:
                entry_website.delete(0, "end")
                entry_pass.delete(0, "end")
                
        else:
            pass

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = tkinter.Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="./Day30_managing_JSON/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

label_website = tkinter.Label(text="Website:", bg=WHITE, font=LABEL_FONT)
label_website.grid(column=0, row=1, sticky="e")
entry_website = tkinter.Entry(width=33)
entry_website.grid(column=1, row=1, columnspan=2, sticky="w")
button_websearch = tkinter.Button(text="Search", width=18, bg=WHITE, font=BUTTON_FONT, command=search_password)
button_websearch.grid(column=2, row=1, sticky="e")
entry_website.focus()
label_email = tkinter.Label(text="Email/Username:", bg=WHITE, font=LABEL_FONT)
label_email.grid(column=0, row=2, sticky="e")
entry_email = tkinter.Entry(width=60)
entry_email.grid(column=1, row=2, columnspan=2, sticky="w")
entry_email.insert(0, "demo@gmail.com")
label_pass = tkinter.Label(text="Password:", bg=WHITE, font=LABEL_FONT)
label_pass.grid(column=0, row=3, sticky="e")
entry_pass = tkinter.Entry(width=33)
entry_pass.grid(column=1, row=3, sticky="w")
button_genpass = tkinter.Button(text="Generate Password", width = 18, bg=WHITE, font=BUTTON_FONT, command=generate_password)
button_genpass.grid(column=2, row=3, sticky="e")
button_add = tkinter.Button(text="Add", width=45, bg=WHITE, font=BUTTON_FONT, command=save_pass)
button_add.grid(column=1, row=4, columnspan=2, sticky="w")








window.mainloop()