import tkinter


def button_clicked():
    my_label["text"] = input.get()
    

window = tkinter.Tk()

window.title("DS GUI")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

# Label
my_label = tkinter.Label(text="Oto labelka", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = tkinter.Button(text="Naduś mnie", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="Naduś mnie 2", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()