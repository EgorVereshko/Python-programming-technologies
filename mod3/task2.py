number = int(input())
print("Неверный ввод" if number < 1 else " ".join([bin(number)[2:], oct(number)[2:], hex(number)[2:]]))