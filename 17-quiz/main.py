from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question['question']
    answer = question['correct_answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you have finished the quiz")
print(f"your final score is {quiz.score} out of {len(question_bank)}")