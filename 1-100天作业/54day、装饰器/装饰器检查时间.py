# #第一题 1.基础装饰器 解答
import time   

# def my_decorator(func):  
#     def wrapper(*args, **kwargs):  
#         start_time = time.time()  
#         print(f'运行的函数名称为{func.__name__}')  
#         print(f'开始运行的时间为{time.strftime("%H:%M:%S", time.localtime(start_time))}')  
#         result = func(*args, **kwargs)  
#         end_time = time.time()  
#         print(f'运行结束的时间为{time.strftime("%H:%M:%S", time.localtime(end_time))}')  
#         print(f'函数运行耗时为{end_time - start_time:.4f}秒')  # 使用 :.4f 来格式化输出，保留四位小数  
#         return result  
#     return wrapper  
  
# @my_decorator  
# def greet(name):  
#     print(f"Hello, {name}!")   
    
# name = 'lili'  
# greet(name)

# #第二题 2.扩展 my_decorator，使其可以接受一个额外的参数 log_level，用于控制是否打印日志。 解答

# def my_decorator(log_level):
#     def wrappers(func):
#         def wrapper(*args,**kwargs):
#             if log_level == "info":
#                 print('打印日志')
#                 start_time = time.time()  
#                 print(f'运行的函数名称为{func.__name__}')  
#                 print(f'开始运行的时间为{time.strftime("%H:%M:%S", time.localtime(start_time))}') 
#                 reult = func(*args,**kwargs)
#                 end_tim = time.time()
#                 print(f'运行结束的时间为{time.strftime("%H:%M:%S", time.localtime(start_time))}') 
#                 print(f'耗费时间为{end_tim - start_time:.4f}秒') 
#             else:
#                 reult = func(*args,**kwargs)       
#             return reult
#         return wrapper
#     return wrappers

# @my_decorator(log_level="info")  
# def greet(name):  
#     print(f"Hello, {name}!")  
  
# greet("Bob")  
  
# # 另一个示例，不打印日志  
# @my_decorator(log_level="silent")  
# def farewell(name):  
#     print(f"Goodbye, {name}!")  
  
# farewell("Charlie")



# #第三题 3.装饰器链 解答


# def decorator_a(func):
#     def my_decorator1(*args,**kwargs):
#         print('正在执行装饰器A')
#         result = func(*args,**kwargs)
#         print('装饰器A执行完毕')
#         return result
#     return my_decorator1

# def decorator_b(func):
#     def my_decorator2(*args,**kwargs):
#         print('正在执行装饰器B')
#         result = func(*args,**kwargs)
#         print('装饰器B执行完毕')
#         return result
#     return my_decorator2

# @decorator_a 
# @decorator_b  
# def my_function():  
#     print("Inside my_function")  
  
# my_function()


#第四题 4.装饰器计算器

def inst(a,b,c):
    return a * b * c
print(inst(1,2,3))


def my_decorator(func):
    def my_decorators(*args):
        print(f'本次执行的函数为{func.__name__}{args}')
        resulnt = func(*args)
        print(f'返回的结果为{resulnt}')
        return resulnt
    return my_decorators

@my_decorator   
def inst(a,b,c):
    return a * b * c
inst(1,2,3) 