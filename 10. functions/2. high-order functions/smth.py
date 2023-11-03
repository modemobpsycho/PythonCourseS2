def high_order_function(func):
    return func(10)


def square(x):
    return x**2


def minus_one(x):
    return x - 1


num1 = high_order_function(square)
num2 = high_order_function(minus_one)

print(num1*num2)