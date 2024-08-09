import html
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
    
    def still_has_questions(self):
        #对比已问的问题和问题列表总数，返回t或者f
        return self.question_number < len(self.question_list)
        #从问题列表获取问题，并发出问询
        #获取用户回答
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        #将html文本符号转义为正常文本
        sss=html.unescape(self.current_question.text)
        self.question_number += 1
        return f"Q.{self.question_number}: {sss}"
        # user_answer = input(f"Q.{self.question_number}: {sss} (True/False): ")
        # self.check_answer(user_answer)
        #获取用户回答如果等于正确答案打印反馈，和更新当前分数。
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
