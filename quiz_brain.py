class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, question_answer, player_answer):
        if question_answer == player_answer:
            print("You got the right answer!")
            self.score += 1
        else:
            print("You got the wrong answer.")
        print(f"The correct answer was: {question_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.")
        print("\n")

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(question.answer, player_answer)


