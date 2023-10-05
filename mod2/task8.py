s, i = input().split(',')

k = 0
for j in range(len(s)-1):
    if s[j] == i:
        k += 1
    else:
        print(k)
        break
