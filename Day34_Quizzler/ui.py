import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 15, "bold")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.text_score = tk.Label(text="Score:", bg=THEME_COLOR, fg="White", font=SCORE_FONT)
        self.text_score.grid(column=1, row=0)
        
        self.canvas = tk.Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=280,
            text="Question", 
            anchor="center", 
            font=QUESTION_FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        # self.curr_question = tk.Label(text="Question", font=QUESTION_FONT)
        # self.curr_question.grid(column=0, row=1, columnspan=2)
        

        self.img_true = tk.PhotoImage(file="./Day34_Quizzler/images/true.png")
        self.button_true = tk.Button(image=self.img_true, highlightthickness=0, command=self.is_true)
        self.button_true.grid(column=0, row=2)
        self.img_false = tk.PhotoImage(file="./Day34_Quizzler/images/false.png")
        self.button_false = tk.Button(image=self.img_false, highlightthickness=0, command=self.is_false)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def is_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.text_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def give_feedback(self, is_right):
        # self.change_canvas_bg(is_right)
        if is_right == True:
            self.canvas.configure(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.configure(bg="red")
            self.window.after(1000, self.get_next_question)
