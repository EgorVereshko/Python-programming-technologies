i, n = input().split(',')

print(chr(97+((ord(i)-97)+int(n))%26))
