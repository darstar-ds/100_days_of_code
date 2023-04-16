import tkinter
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
HEADER_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

def update_word():
    global flip_after_3s
    global en_word
    window.after_cancel(flip_after_3s)
    f_word, en_word = select_word()
    canvas.itemconfig(tagOrId=card_word, text=f_word, fill="black")
    canvas.itemconfig(tagOrId=card_title, text="French", fill="black")
    canvas.itemconfig(tagOrId=curr_card, image=img_card_front)
    flip_after_3s = window.after(3000, flip_card)

def i_know_the_word():
    global flip_after_3s
    global en_word
    global f_word
    global dict_of_fr_words
    window.after_cancel(flip_after_3s)
    
    # remove the current word that I know
    dict_of_fr_words = [i for i in dict_of_fr_words if not (i['French'] == f_word)]
    # convert current lis to dataframe and save as csv
    df = pd.DataFrame(dict_of_fr_words)
    df.to_csv("./Day31_Flash_Card_project/data/words_to_learn.csv", index=False)
    
    f_word, en_word = select_word()
    canvas.itemconfig(tagOrId=card_word, text=f_word, fill="black")
    canvas.itemconfig(tagOrId=card_title, text="French", fill="black")
    canvas.itemconfig(tagOrId=curr_card, image=img_card_front)
    flip_after_3s = window.after(3000, flip_card)

def select_word():
    dict_selected = random.choice(dict_of_fr_words)
    f_word = dict_selected["French"]
    en_word = dict_selected["English"]
    return f_word, en_word

def flip_card():
    canvas.itemconfig(tagOrId=curr_card, image=img_card_back)
    canvas.itemconfig(tagOrId=card_title, text="English", fill="white")
    canvas.itemconfig(tagOrId=card_word, text=en_word, fill="white")

def dict_of_f_words():
    is_words2learn = os.path.isfile("./Day31_Flash_Card_project/data/words_to_learn.csv")
    if is_words2learn:
        df = pd.read_csv("./Day31_Flash_Card_project/data/words_to_learn.csv")
    else:    
        df = pd.read_csv("./Day31_Flash_Card_project/data/french_words.csv")
        df.head()
        df.to_csv("./Day31_Flash_Card_project/data/words_to_learn.csv", index=False)
    dict_of_f_words = df.to_dict(orient="records")
    return dict_of_f_words

dict_of_fr_words = dict_of_f_words()
print(dict_of_fr_words)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_card_front = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/card_front.png")
img_card_back = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/card_back.png")
curr_card = canvas.create_image(400, 263, image=img_card_front)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="French", font=HEADER_FONT)
f_word, en_word = select_word()
card_word = canvas.create_text(400, 263, text=f_word, font=WORD_FONT)


img_iknow = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/right.png")
button_iknow = tkinter.Button(image=img_iknow, highlightthickness=0, command=i_know_the_word)
button_iknow.grid(column=0, row=1)
img_idontknow = tkinter.PhotoImage(file="./Day31_Flash_Card_project/images/wrong.png")
button_idontknow = tkinter.Button(image=img_idontknow, highlightthickness=0, command=update_word)
button_idontknow.grid(column=1, row=1)

flip_after_3s = window.after(3000, flip_card)


window.mainloop()