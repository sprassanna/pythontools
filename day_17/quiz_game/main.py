from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for eachData in question_data:
    question_bank.append(Question(question=eachData['text'], answer=eachData['answer']))

my_quiz = QuizBrain(question_bank)

while my_quiz.still_has_questions():
    my_quiz.next_question()

print(f'The final score is {my_quiz.score} / {len(my_quiz.question_list)}')
