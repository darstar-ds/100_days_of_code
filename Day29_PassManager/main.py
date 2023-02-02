import tkinter
WHITE="#FFFFFF"
LABEL_FONT=("Arial", 12, "bold")
BUTTON_FONT=("Arial", 10, "bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    with open("./Day29_PassManager/my_pass.txt", "a") as passfile:
        website=entry_website.get()
        entry_website.delete(0, "end")
        email=entry_email.get()
        # entry_email.delete(0, "end")
        # entry_email.insert(0, "demo@gmail.com")
        password=entry_pass.get()
        entry_pass.delete(0, "end")
        passfile.write("\n" + website + " | " + email + " | " + password)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = tkinter.Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="./Day29_PassManager/logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

label_website = tkinter.Label(text="Website:", bg=WHITE, font=LABEL_FONT)
label_website.grid(column=0, row=1, sticky="e")
entry_website = tkinter.Entry(width=60)
entry_website.grid(column=1, row=1, columnspan=2, sticky="w")
entry_website.focus()
label_email = tkinter.Label(text="Email/Username:", bg=WHITE, font=LABEL_FONT)
label_email.grid(column=0, row=2, sticky="e")
entry_email = tkinter.Entry(width=60)
entry_email.grid(column=1, row=2, columnspan=2, sticky="w")
entry_email.insert(0, "demo@gmail.com")
label_pass = tkinter.Label(text="Password:", bg=WHITE, font=LABEL_FONT)
label_pass.grid(column=0, row=3, sticky="e")
entry_pass = tkinter.Entry(width=35)
entry_pass.grid(column=1, row=3, sticky="w")
button_genpass = tkinter.Button(text="Generate Password", bg=WHITE, font=BUTTON_FONT)
button_genpass.grid(column=2, row=3, sticky="e")
button_add = tkinter.Button(text="Add", width=44, bg=WHITE, font=BUTTON_FONT, command=save_pass)
button_add.grid(column=1, row=4, columnspan=2, sticky="w")








window.mainloop()