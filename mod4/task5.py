from collections import Counter


def count_letters(file_name):
    with open(file_name, 'r') as file:
        content = file.read().lower()

    counter = Counter(c for c in content if c.isalpha())

    sorted_stats = sorted(counter.items(), key=lambda x: x[1])

    # Открываем файл для записи результатов
    with open('stats.txt', 'w') as file:
        for letter, count in sorted_stats:
            file.write(f"{letter}: {count}\n")


file_name = input("Введите имя файла: ")
count_letters(file_name)
