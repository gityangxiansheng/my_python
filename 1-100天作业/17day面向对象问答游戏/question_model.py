from data import question_data


class Question:
    def __init__(self,文字,答案):
        self.文字=文字
        self.答案=答案
    def prints(self):
        print(self.文字)
        print(type(self.文字))
        print(self.答案)
        print(type(self.答案))