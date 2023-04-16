import tkinter as tk


THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 15, "bold")


class QuizInterface:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.text_score = tk.Label(text="Score:", bg=THEME_COLOR, fg="White", font=SCORE_FONT)
        self.text_score.grid(column=1, row=0)
        
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.q_text = self.canvas.create_text(1, 1, text="Question", anchor="nw", font=QUESTION_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        # self.curr_question = tk.Label(text="Question", font=QUESTION_FONT)
        # self.curr_question.grid(column=0, row=1, columnspan=2)
        

        self.img_true = tk.PhotoImage(file="./Day34_Quizzler/images/true.png")
        self.button_true = tk.Button(image=self.img_true, highlightthickness=0, command=self.check_answer)
        self.button_true.grid(column=0, row=2)
        self.img_false = tk.PhotoImage(file="./Day34_Quizzler/images/false.png")
        self.button_false = tk.Button(image=self.img_false, highlightthickness=0, command=self.check_answer)
        self.button_false.grid(column=1, row=2)



        self.window.mainloop()

    def check_answer(self):
        pass