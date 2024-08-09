class MenuItem:
    """ 模拟每个菜单项 """
    def __init__(self, name, water, milk, coffee, cost):
        """ 初始化方法，设置菜单项的属性 """
        self.name = name  # 菜单项的名称
        self.cost = cost  # 菜单项的价格
        self.ingredients = {
            "water": water,  # 水的量
            "milk": milk,  # 牛奶的量
            "coffee": coffee  # 咖啡的量
        }  # 包含菜单项所需材料的字典

class Menu:
    """ 模拟带有饮料的菜单 """
    def __init__(self):
        """ 初始化方法，设置菜单的属性 """
        self.menu = [
            MenuItem(name="拿铁", water=200, milk=150, coffee=24, cost=2.5),  # 拿铁的材料和价格
            MenuItem(name="浓缩咖啡", water=50, milk=0, coffee=18, cost=1.5),  # 浓缩咖啡的材料和价格
            MenuItem(name="卡布奇诺", water=250, milk=50, coffee=24, cost=3)  # 卡布奇诺的材料和价格
        ]  # 菜单中的菜单项列表

    def get_items(self):
        """ 返回所有可用菜单项的名称 """
        options = ""  # 用于存储菜单项名称的字符串
        for item in self.menu:
            options += f"{item.name}/"  # 将每个菜单项的名称添加到 options 字符串中
        return options  # 返回包含所有菜单项名称的字符串

    def find_drink(self, order_name):
        """ 按名称搜索菜单中的特定饮料。如果存在，则返回该项，否则返回 None """
        for item in self.menu:
            if item.name == order_name:
                return item  # 如果找到名称匹配的菜单项，则返回该项
        print("抱歉，该项目不可用。")  # 如果未找到，则打印提示信息
        
        

