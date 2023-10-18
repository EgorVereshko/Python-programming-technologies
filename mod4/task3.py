def func(a, b):
    if b == 0:
        return a
    else:
        return func(b, a % b)


number1 = int(input())
number2 = int(input())

print(func(number1, number2))
