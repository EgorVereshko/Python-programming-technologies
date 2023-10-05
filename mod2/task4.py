number = int(input())

if number < 1:
    print("Неверный ввод")
    
else:
    string_bin = ""
    num1 = number
    while num1 > 0:
        string_bin = str(num1 % 2) + string_bin
        num1 //= 2

    string_oct = ""
    num2 = number
    while num2 > 0:
        string_oct = str(num2 % 8) + string_oct
        num2 //= 8

    string_hex = ""
    num3 = number
    while num3 > 0:
        string_hex = str(num3 % 16) + string_hex
        num3 //= 16

    print(string_bin, string_oct, string_hex)
