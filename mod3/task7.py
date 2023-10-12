numbers = input().split(' ')
print(True if sorted(numbers) != sorted(set(numbers)) else False)

