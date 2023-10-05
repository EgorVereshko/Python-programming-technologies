s = input().replace(' ', '')

vowel = ['а', 'е', 'о', 'и', 'у', 'ю', 'э', 'ё', 'ы']
vowel_count = 0

for i in range(len(s)):
    if s[i] in vowel:
        vowel_count += 1
    consonant_count = len(s) - vowel_count
        
print(vowel_count, consonant_count)
