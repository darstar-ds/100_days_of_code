import tkinter

window = tkinter.Tk()
window.title("Miles 2 Kilometers calculator")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

def mile2km(miles):
    km = float(miles) * 1.609
    return km

def update_result():
    # print(f"Type of entry_miles.get(): {type(entry_miles.get())}")
    result = float(mile2km(entry_miles.get()))
    # print(f"Type of result: {type(result)}")
    label_result["text"] = str("%.3f" % result)

label_miles = tkinter.Label(text="miles", font=("Arial", 16, "bold"))
label_miles.grid(column=2, row=0)
label_is_eq = tkinter.Label(text="is equal to", font=("Arial", 16, "bold"))
label_is_eq.grid(column=0, row=1)
label_km = tkinter.Label(text="km", font=("Arial", 16, "bold"))
label_km.grid(column=2, row=1)
button_calc = tkinter.Button(text="Calculate", font=("Arial", 16, "normal"), command=update_result)
button_calc.grid(column=1, row=2)
entry_miles = tkinter.Entry(width=10, font=("Arial", 16, "normal"))
entry_miles.grid(column=1, row=0)
label_result = tkinter.Label(text="0", width=10, font=("Arial", 16, "bold"))
label_result.grid(column=1, row=1)




window.mainloop()
