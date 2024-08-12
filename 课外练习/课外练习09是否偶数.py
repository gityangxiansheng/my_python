# number = 10

# if number % 2 == 0:
#     print("这是一个偶数！")
# else:
#     print("这不是一个偶数！")


for number in range(1,101):
    if number % 3 ==0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

