

def logging_decorator(cs):
    def logging_decorator_in(*args):
        rec = cs(*args)
        print(f"运行{cs.__name__}{args}函数,结果为{rec}")
        return rec
    return logging_decorator_in


@logging_decorator
def a_function(a,b,c):
    return a*b*c

ccq = a_function(1,2,3)
print(ccq)