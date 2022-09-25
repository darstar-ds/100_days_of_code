class QuizBrain:

    def __init__(self, q_texts):
        self.question_number = 0
        self.question_list = q_texts
        self.user_score = 0
 

    def still_have_questions(self):
        return self.question_number < len(self.question_list)


    def next_question(self):
        curr_q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {curr_q.text} (True/False)?: ")    
        self.check_answer(user_answer, curr_q.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.user_score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is {self.user_score}/{self.question_number}")
        print("\n")