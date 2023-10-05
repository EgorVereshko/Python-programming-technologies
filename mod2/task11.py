sequence = input()
flag = False
for i in range(len(sequence)):
    for j in range(len(sequence)):
        if i != j:
            if sequence[i] == sequence[j] and sequence[i] != " ":
                flag = True
                break
print(flag)
