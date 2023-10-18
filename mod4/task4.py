word = input()
result = ''
odd_count = 0
odd_letter = ''

letter_count = {}
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

for letter, count in letter_count.items():
    if count % 2 != 0:
        odd_count += 1
        odd_letter = letter

    result += letter * (count // 2)

if odd_count > 1:
    print("Из слова нельзя составить палиндром")
else:
    result += odd_letter + result[::-1]
    print(result)
