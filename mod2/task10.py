string = input()
result = ""
k = ''
for i in range(len(string)-1):
    if string[i] == ' ':
        result += string[i-1]
print(result)
