#闰年计算器项目9
def years(year):  
    if year % 4 ==0:

        if year % 100 ==0:
            
            if year % 400 ==0:
                # print(str(year)+"闰年")
                return True
            else:
                # print(str(year)+"not闰年")
                return False
        else:
            # print(+str(year)+"闰年")
            return True
    else:
        # print(str(year)+"not闰年")
        return False

def days_in_month (month,year):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    print(month)
    if month > 12 and month < 0 :
        return "无效输入！"
    else:
        if years(year) == False:
            if month == 2:
                return 29
            else:
                return month_days[month-1]
        elif years(year) == True:
            return month_days[month-1]
        
year=int(input("你要查那一年？\n"))
month=int(input("你要查几月份？\n"))
days=days_in_month (month,year)
print(days)

