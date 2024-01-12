from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for dict in question_data:
    question_bank.append(Question(dict["question"], dict["correct_answer"]))

quiz_b = QuizBrain(question_bank)

while quiz_b.still_has_question():
    quiz_b.next_question()


print("You've completed the quiz.")
print(f"Your final score was: {quiz_b.score}/{quiz_b.question_number}.")
