from data import question_data
from question_model import Question
from quiz_brain import quiz

question_bank = []

for s in question_data:
    questions_文字=s["question"]
    questions_答案=s["correct_answer"]
    questions=Question(questions_文字,questions_答案)
    question_bank.append(questions)

# print(question_bank[0].d)
提问=quiz(question_bank)


while 提问.still_has_questions()[0]:
    提问.next_question()
print("恭喜您完成所有问答!")    
print(f"您的最终分数是{提问.still_has_questions()[1]}")

    # questions.prints
# series=1
# for s in question_data :
#     print(f"Q{series}.{s["文字"]}")
#     user=input("请输入正确或者错误\n")
#     if user == "正确" or user == "错误":
#         if user == s["答案"]:
#             print("恭喜你答对了!")
#             print(f"正确的答案是{s["答案"]}!")
#             print(f"您现在的分数是{series}/{series}")
#             series += 1
#         else:
#             print("抱歉你答错了!")
#             print(f"正确的答案是{s["答案"]}!")
#             print(f"您现在的分数是{series-1}/{series}")
#             break
#     else:
#         print("您的输入有误!")
#         break