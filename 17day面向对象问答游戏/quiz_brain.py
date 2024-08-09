class quiz:
    def __init__(self,question_list):
        self.question_list=question_list
        self.question_number=0
        self.score = 0
    def still_has_questions(self):
        最终分数=f"{self.score}/{self.question_number}"
        # print(f"最后分数是：{最终分数}")
        return self.question_number<len(self.question_list),最终分数
    
    def next_question(self):
        number=self.question_number
        self.question_number += 1
        # print("序号",number)
        # print("长度是",self.question_number)
        print(f"Q{self.question_number}:{self.question_list[number].文字}") 
        user=input("请输入正确或者错误\n")
        答案=self.question_list[number].答案
        self.check_answer(user,答案)
            
    def check_answer(self,user, 答案):
        if user == "True" or user == "False":
            if user == 答案:
                self.score+=1
                print("恭喜你答对了!")
                print(f"正确的答案是{答案}!")
                print(f"您现在的分数是{self.score}/{self.question_number}")
            else:
                print("抱歉你答错了!")
                print(f"正确的答案是{答案}!")
                print(f"您现在的分数是{self.score}/{self.question_number}")
                # self.question_number+=10
        else:
            print("您的输入有误!")
            # self.question_number+=10
            
        print("\n")