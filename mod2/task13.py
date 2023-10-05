numbers = input()

result1 = 0
result2 = 0
for i in range(0, len(numbers), 1):
    result1 += int(numbers[i])
for j in range(1, len(numbers), 1):
    result2 += int(numbers[j])

if (result1 + result2) % 10 == 0:
    print('yes')
else:
    print('no')
