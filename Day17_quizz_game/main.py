from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
print(len(question_data))

for question in question_data:
    local_question_text = question["question"]
    local_question_answer = question["correct_answer"]
    local_question = Question(local_question_text, local_question_answer)
    question_bank.append(local_question)

# print(question_bank[1].text)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.user_score}/{quiz.question_number}")
