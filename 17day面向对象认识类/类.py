class Student:
    def __init__(self,student_name,student_id):
        self.name = student_name
        self.id = student_id
        self.grades = {"语文":0,"数学":0,"英语":0}

    def set_grades(self,科目,分数):
        if 科目 in self.grades:
            self.grades[科目]=分数

    def print_grades(self):
        print(f"学生{self.name}（学号：{self.id}）")
        for 科目 in self.grades:
            print(f"{科目}：{self.grades[科目]}分")



张三 = Student("张三",2)
李四 = Student("李四",5)


李四.set_grades("数学",95)
李四.set_grades("英语",90)
李四.set_grades("语文",60)
李四.print_grades() 