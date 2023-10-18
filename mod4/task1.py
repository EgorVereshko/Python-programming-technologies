def func(spisok):
    if len(set(spisok)) == 1:
        return "Все числа равны"
    elif len(set(spisok)) == len(spisok):
        return "Все числа разные"
    else:
        return "Есть равные и неравные числа"


spisok = input().split()
spisok = [int(number) for number in spisok]

print(func(spisok))
