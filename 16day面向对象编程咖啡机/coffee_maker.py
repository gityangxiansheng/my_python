class CoffeeMaker:
    """ 模拟制作咖啡的机器 """
    def __init__(self):
        """ 初始化方法，设置资源 """
        self.resources = {
            "water": 300,  # 水：300ml
            "milk": 200,  # 牛奶：200ml
            "coffee": 100  # 咖啡：100g
        }

    def report(self):
        """ 打印所有资源的报告 """
        print(f"水：{self.resources['water']}ml")  # 打印出水的量
        print(f"牛奶：{self.resources['milk']}ml")  # 打印出牛奶的量
        print(f"咖啡：{self.resources['coffee']}g")  # 打印出咖啡的量

    def is_resource_sufficient(self, drink):
        """ 当订单可以制作时返回 True，当材料不足时返回 False """
        can_make = True  # 假设订单可以制作
        for item in drink.ingredients:  # 遍历订单的材料
            if drink.ingredients[item] > self.resources[item]:  # 如果订单所需的材料数量超过现有资源的数量
                print(f"抱歉，没有足够的{item}.")  # 打印出材料不足的信息
                can_make = False  # 更新订单是否可以制作的状态
        return can_make  # 返回订单是否可以制作的结果

    def make_coffee(self, order):
        """ 从资源中扣除所需的材料 """
        for item in order.ingredients:  # 遍历订单的材料
            self.resources[item] -= order.ingredients[item]  # 从资源中扣除所需的材料数量
        print(f"这是你的{order.name} ☕️. 请享用!")  # 打印出制作完成的咖啡名称