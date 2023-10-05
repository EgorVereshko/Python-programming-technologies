string = input()
string += ' '
result = ""
for i in range(len(string)):
    if string[i] == ' ':
        result += string[i-1]
print(result)
