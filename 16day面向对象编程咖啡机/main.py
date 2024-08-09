from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


菜单 = Menu()
咖啡机 = CoffeeMaker()
投币机 = MoneyMachine()



# 咖啡机.report()
# 投币机.report()
state="开机"
while state == "开机":
    input_menu = input(f"请问你需要点儿什么？{菜单.get_items()}")
    if input_menu == "报告":
        咖啡机.report()
        投币机.report()
    elif  input_menu == "关闭":
        state="关闭"
        break
    else :
        item = 菜单.find_drink(input_menu)
        if 咖啡机.is_resource_sufficient(item) and 投币机.make_payment(item.cost):
                咖啡机.make_coffee(item)
        