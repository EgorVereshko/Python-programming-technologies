sequence = input()
sequence.replace(' ', '')
for i in range(len(sequence)-1):
    for j in range(len(sequence)):
        print(sequence[i] == sequence[j])
        break
    break
