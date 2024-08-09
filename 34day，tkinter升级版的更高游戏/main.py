from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizIntenrface

#新建列表
question_bank = []
#循环问题字典，遍历问题
for question in question_data:
    #从字典中找到问题，储存至变量中
    question_text = question["question"]
    #从字典中找到答案，储存至变量中
    question_answer = question["correct_answer"]
    #将问题和答案组合在一块储存至question_bank列表中
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#将列表导入QuizBrain类
quiz = QuizBrain(question_bank)

ui = QuizIntenrface(quiz)




#循环类中的still_has_questions函数
# while quiz.still_has_questions():
#     quiz.next_question()
#如果十个题目全部答完反馈
print("你完成了测验")
print(f"你的最终分数是: {quiz.score}/{quiz.question_number}")



