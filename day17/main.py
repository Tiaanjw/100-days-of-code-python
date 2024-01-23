from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

quiz_system = QuizBrain(question_bank) 

while quiz_system.still_has_questions():
    quiz_system.next_question()
    
print(f"Quiz completed, your score {quiz_system.score}/{quiz_system.question_number}")