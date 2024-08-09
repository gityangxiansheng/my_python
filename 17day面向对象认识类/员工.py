class Staff:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def print_info(self):
        print(f"姓名：{self.name}，工号：{self.id}")


class FullTime(Staff):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary=monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary
        # print(f"他的月薪是{self.monthly_salary}元")

class PartTime(Staff):
    def __init__(self,name,id,monthly_days,work_days):
        super().__init__(name,id)
        self.monthly_days=monthly_days
        self.work_days=work_days

    def calculate_monthly_salary(self):

        # print(f"他的月薪是{(self.monthly_days*self.work_days)}元")
        return self.monthly_days*self.work_days


zhangsan=FullTime("张三","0521",10330)
lisi = PartTime("李四","0520",165,30)

zhangsan.print_info()
print(zhangsan.calculate_monthly_pay())

lisi.print_info()
# lisi.calculate_monthly_salary()
print(lisi.calculate_monthly_salary())
