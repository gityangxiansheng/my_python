class MoneyMachine:
    """
    货币机类
    CURRENCY：货币符号，这里默认是"$"
    COIN_VALUES：硬币的价值字典，包括"quarters"（25 美分）、"dimes"（10 美分）、"nickles"（5 美分）和"pennies"（1 美分）
    """
    CURRENCY = "$"  # 货币符号，这里默认是"$"
    COIN_VALUES = {
        "quarters": 0.25,  # 25 美分的价值
        "dimes": 0.10,  # 10 美分的价值
        "nickles": 0.05,  # 5 美分的价值
        "pennies": 0.01  # 1 美分的价值
    }

    def __init__(self):
        """
        初始化方法
        self.profit：利润
        self.money_received：收到的钱
        """
        self.profit = 0  # 利润
        self.money_received = 0  # 收到的钱

    def report(self):
        """ 
        打印当前利润
        """
        print(f"钱：{self.CURRENCY}{self.profit}")  # 打印利润

    def process_coins(self):
        """ 
        处理插入的硬币，返回计算出的总金额
        提示用户插入硬币
        对于每种硬币，获取用户输入的数量并乘以硬币的价值，累加到 self.money_received
        """
        print("请插入硬币。")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"有多少{coin}?：")) * self.COIN_VALUES[coin]  # 获取用户输入的硬币数量并累加到总金额

    def make_payment(self, cost):
        """ 
        判断支付是否被接受
        处理硬币
        如果收到的钱大于或等于成本，计算找零并打印，增加利润，重置 self.money_received
        否则，打印提示信息并重置 self.money_received
        返回支付是否被接受的布尔值
        """
        self.process_coins()  # 处理硬币
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)  # 计算找零
            print(f"这是{self.CURRENCY}{change}的零钱。")
            self.profit += cost  # 增加利润
            self.money_received = 0  # 重置收到的钱
            return True  # 支付被接受
        else:
            print("抱歉，钱不够。已退款。")
            self.money_received = 0  # 重置收到的钱
            return False  # 支付未被接受