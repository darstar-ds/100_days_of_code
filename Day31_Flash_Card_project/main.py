import tkinter
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
HEADER_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

def update_f_word():
    f_word = select_f_word()
    canvas.itemconfig(tagOrId=card_f_word, text=f_word)

def select_f_word():
    dict_selected = random.choice(dict_of_f_words)
    f_word = dict_selected["French"]
    return f_word

df = pd.read_csv("./Day31_Flash_Card_project/data/french_words.csv")
dict_of_f_words = df.to_dict(orient="records")


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_card_front = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/card_front.png")
img_card_back = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/card_back.png")
canvas.create_image(400, 263, image=img_card_front)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="French", font=HEADER_FONT)
f_word = select_f_word()
card_f_word = canvas.create_text(400, 263, text=f_word, font=WORD_FONT)


img_iknow = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/right.png")
button_iknow = tkinter.Button(image=img_iknow, highlightthickness=0, command=update_f_word)
button_iknow.grid(column=0, row=1)
img_idontknow = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/wrong.png")
button_idontknow = tkinter.Button(image=img_idontknow, highlightthickness=0, command=update_f_word)
button_idontknow.grid(column=1, row=1)




window.mainloop()