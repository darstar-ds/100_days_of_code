import tkinter

BACKGROUND_COLOR = "#B1DDC6"
HEADER_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
img_card_front = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/card_front.png")
img_card_back = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/card_back.png")
canvas.create_image(400, 264, image=img_card_front)
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(400, 150, text="French", font=HEADER_FONT)
canvas.create_text(400, 263, text="trouve", font=WORD_FONT)


img_iknow = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/right.png")
button_iknow = tkinter.Button(image=img_iknow, highlightthickness=0)
button_iknow.grid(column=0, row=1)
img_idontknow = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/wrong.png")
button_idontknow = tkinter.Button(image=img_idontknow, highlightthickness=0)
button_idontknow.grid(column=1, row=1)







window.mainloop()