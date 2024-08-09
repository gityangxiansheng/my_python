def outer(origin):
    def inner(*args):
        print("准备执行函数！！")
        res = origin(*args)
        print("函数执行完毕！！")
        return res
    return inner

@outer
def func1(*args):
    print("我是函数func")
    # value = (2,4,6,8,10)
    c=sum(args)
    print("函数结束")
    return c
@outer
def func2():
    print("我是函数func")
    value = (2,4,6,8,10)
    print("函数结束")
    return value
@outer
def func3():
    print("我是函数func")
    value = (2,4,6,8,10)
    print("函数结束")
    return value





result1 = func1(1,1,1,1,1,1,1,1,1)
result2 = func2()
result3 = func3()
print(f'返回结果{result1}')
